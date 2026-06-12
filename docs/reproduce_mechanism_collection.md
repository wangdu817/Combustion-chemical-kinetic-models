# Combustion and Flame 机理收集复现与续接流程

本文档说明如何复现当前项目的论文机理附件收集、整理、总结和断点续接流程。默认目标是减少重复网页访问和重复下载：已经完成探测、下载或处理的文章不会再次执行对应步骤，除非显式使用 `--force`。

## 1. 输出结构

项目根目录为 `E:\mech_collection`，主要输出目录为：

```text
combustion_and_flame_mechanisms/
  fuel_type/
    year/
      firstauthorsurname_year_fueltype_articlenumber/
        mechanism_summary.md
        chem.inp
        therm.dat
        tran.dat
        mechanism.yaml
        _processing/
  collection_index.csv
  manual_download_handoff.md
  run_summary.json
  _raw/
    article_metadata.json
    downloads/
```

顶层论文文件夹只保留总结文件和标准化机理文件。原始附件、递归解压结果、Cantera 转换日志和中间文件保存在对应论文文件夹的 `_processing/` 子目录。Git 默认不跟踪 PDF、附件、机理大文件和 `_processing/` 目录，只跟踪脚本、索引、元数据和总结。

## 2. 环境要求

- Windows + PowerShell。
- 当前仓库：`E:\mech_collection`。
- Python：`C:\Users\17915\anaconda3\envs\analysis-env\python.exe`。
- Python 环境需要可导入 Cantera 和 PyYAML。
- Chrome 已登录 ScienceDirect/Elsevier。流程不读取、不导出密码、cookie、localStorage 或浏览器 session 文件。
- 可选：`7z` 用于解压 `.rar` 和 `.7z`；`curl.exe` 用于部分 Elsevier CDN 下载 fallback。

快速检查：

```powershell
cd E:\mech_collection
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' -c "import cantera, yaml; print(cantera.__version__)"
git status --short --branch
```

## 3. 状态记录和断点续接规则

每篇文章的状态记录保存在 `combustion_and_flame_mechanisms/_raw/article_metadata.json`，汇总表保存在 `collection_index.csv`。

关键字段：

- `supplementProbeStatus`: `complete`、`no_links`、`captcha`、`error`、`partial`。
- `supplementProbeCheckedAt`: 最近一次附件链接探测时间。
- `supplementDownloadStatus`: `complete`、`partial`、`failed`、`none`。
- `downloadStatus`: 每个附件链接的下载状态，常见值为 `downloaded`、`existing`、`failed`。
- `processingStatus`: `included`、`conversion_failed`、`excluded_no_mechanism_attachment`、`excluded_no_supplement_found`、`excluded_no_mechanism_signal` 等。
- `processedAt`: 最近一次实际处理附件和 Cantera 转换的时间。
- `processingFolder`: 该文章对应的输出文件夹。

默认规则：

- `probe-supplements` 会跳过已经有终态 `supplementProbeStatus` 的文章。
- `download-supplements` 会跳过已经完整下载、已经失败或部分失败的文章；失败链接不会反复重试。
- `process` 会优先复用已有 `collection_index.csv` 和现有论文文件夹，默认不再重复复制附件、递归解压或执行 Cantera。
- 只有确认需要重新跑某一步时才加 `--force`。

## 4. 年份元数据导入

ScienceDirect 卷期页面采集结果应保存为 JSON 文件，例如：

```text
combustion_and_flame_mechanisms/_raw/2025_volumes/volume_*.json
```

每条记录至少应包含：

- `year`
- `volume`
- `month`
- `title`
- `authors`
- `doi`
- `pii`
- `articleNumber`
- `url`
- `issuePdfLink`

导入命令：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py import-sciencedirect-metadata --year 2025 --source-dir combustion_and_flame_mechanisms\_raw\2025_volumes
```

如果需要导入 2026：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py import-sciencedirect-metadata --year 2026 --source-dir combustion_and_flame_mechanisms\_raw\2026_volumes
```

## 5. 候选筛选和本地处理

先运行一次处理命令，让脚本根据题名和摘要标记反应动力学候选，并从已有下载中识别机理：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py process
```

该命令会：

- 检测燃料类型。
- 判断是否属于反应动力学候选。
- 复制已有附件到文章 `_processing/raw_downloads/`。
- 对附件递归解压，最大深度为 5 层。
- 按文件内容识别 CHEMKIN、Cantera、热力学和输运文件。
- 将标准机理命名为 `chem.inp`，热力学文件命名为 `therm.dat`，输运文件命名为 `tran.dat`。
- 调用 Cantera 的 `ck2yaml`，使用 `--permissive`，并生成 `mechanism.yaml`。
- 从 Cantera 或 YAML 结果读取物种数和反应数。
- 写入每篇文章的 `mechanism_summary.md`，其中包含摘要、燃料类型、验证反应器类型、GB/T 7714 格式参考文献、物种数和反应数。

默认运行时会跳过已完成处理的文章。确实需要全量重跑时：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py process --force
```

## 6. 附件链接探测和下载

先使用 Elsevier CDN 的可预测 `mmc` 链接探测附件：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py probe-supplements --year 2025 --max-mmc 12
```

默认会跳过已经标记为 `complete`、`no_links`、`captcha`、`error` 或 `partial` 的文章。需要重新探测时：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py probe-supplements --year 2025 --max-mmc 12 --force
```

下载已经记录的附件链接：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py download-supplements --year 2025
```

如果某些链接失败，后续默认不会反复重试。确认 ScienceDirect 登录、网络或 CAPTCHA 状态已解决后再使用：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py download-supplements --year 2025 --force
```

下载完成后重新运行：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py process
```

## 7. 文章页附件链接导入

当直接 `mmc` 探测无法确认附件时，可用已登录 Chrome 打开 ScienceDirect 文章页并采集页面中的 supplementary material 链接。采集结果保存为：

```text
combustion_and_flame_mechanisms/_raw/2025_supplement_links/chunk_*.json
```

每条记录格式：

```json
{
  "pii": "S0010218025000000",
  "url": "https://www.sciencedirect.com/science/article/pii/S0010218025000000",
  "captcha": false,
  "links": [
    {
      "href": "https://ars.els-cdn.com/content/image/1-s2.0-S0010218025000000-mmc1.zip",
      "text": "Supplementary material"
    }
  ]
}
```

导入页面采集结果：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py import-page-supplements --source-dir combustion_and_flame_mechanisms\_raw\2025_supplement_links
```

若遇到 CAPTCHA、机构 SSO 或权限不足，不要绕过验证。让用户在 Chrome 中完成验证，然后继续采集。无法自动完成的项目会保留在 `manual_download_handoff.md`。

## 8. 摘要补充

摘要优先来自本地 PDF，其次来自 Crossref、OpenAlex 和 Semantic Scholar。补充命令：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py enrich-abstracts
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' scripts\collect_cf2026.py process
```

摘要无法确认验证反应器类型时，`mechanism_summary.md` 中应写 `not clear from abstract`，不要从全文或常识推断。

## 9. 质量检查

每轮实际新增或重处理后运行：

```powershell
& 'C:\Users\17915\anaconda3\envs\analysis-env\python.exe' -m unittest discover -s tests
```

再检查索引和未完成项：

```powershell
Import-Csv combustion_and_flame_mechanisms\collection_index.csv | Group-Object status | Select-Object Name,Count
Get-Content combustion_and_flame_mechanisms\manual_download_handoff.md | Select-Object -First 80
```

确认无重复 DOI：

```powershell
Import-Csv combustion_and_flame_mechanisms\collection_index.csv |
  Where-Object doi |
  Group-Object doi |
  Where-Object Count -gt 1
```

## 10. 提交和推送

提交前确认没有把 PDF、压缩包、原始附件、日志或 `_processing/` 内容加入 Git：

```powershell
git status --short
git add scripts README.md docs combustion_and_flame_mechanisms\README.md combustion_and_flame_mechanisms\collection_index.csv combustion_and_flame_mechanisms\manual_download_handoff.md combustion_and_flame_mechanisms\run_summary.json combustion_and_flame_mechanisms\_raw\article_metadata.json
git diff --cached --name-only
```

如果 staged 文件中出现 `.pdf`、`.zip`、`.rar`、`.7z`、`.inp`、`.dat`、`.yaml`、`_processing` 或 `_raw/downloads`，需要先取消暂存这些文件。

提交和推送：

```powershell
git commit -m "Add resumable collection workflow"
git push origin master
```

## 11. 常见续接场景

- 新增年份：导入该年份卷期 JSON，运行 `process`，然后按需 `probe-supplements --year <year>`、`download-supplements --year <year>`、`process`。
- CAPTCHA 后继续：用户在 Chrome 完成验证后，重新执行被中断的页面采集；已完成记录不会被重复访问。
- 失败链接重试：只对确认需要重试的年份使用 `download-supplements --year <year> --force`。
- 燃料识别错误：更新 `FUEL_PATTERNS` 后运行 `process --force`。不加 `--force` 时会优先复用旧索引。
- Cantera 转换规则调整：修改转换或清理逻辑后运行 `process --force`，并抽查 `mechanism_summary.md`、`mechanism.yaml` 和 `_processing/*conversion*.log`。
