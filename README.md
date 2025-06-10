## 功能

*   自动添加许可证头部:  如果文件缺少许可证头部，脚本会自动添加或更新
*   支持文件类型:
    *   `.java`
    *   `.ftl`
    *   `.yml` 和 `.yaml`
    *   `.md`

## 忽略规则

`ignore_patterns` 定义了要排除的文件和目录

```python
ignore_patterns = [
        'LICENSE',
        'NOTICE',
        'DISCLAIMER',
        '*.json',
        '.github/**',
        '.git/**',
]
```
