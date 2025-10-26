# Ascbinary / ASCII与二进制转换器

[English](#english) | [中文](#chinese)

<a name="chinese"></a>
## 中文说明

### 项目简介
这是一个简单的Python工具，用于在ASCII字符和二进制表示之间进行相互转换。支持中英文双语界面。

### 功能特点
- ASCII文本转二进制
- 二进制转ASCII文本
- 中英文双语界面
- 基于JSON配置的本地化系统

### 使用方法
1. 确保已安装Python 3.x
2. 准备必要的JSON配置文件：
   - `locals.json` - 包含界面文本的本地化字符串
   - `ascii_char_to_binary.json` - 包含ASCII字符到二进制的映射表
3. 运行程序：
   ```bash
   python Ascbinary.py
   ```
4. 按照提示操作：
   - 首先选择界面语言（1-中文，2-英文）
   - 然后选择转换模式（1-ASCII转二进制，2-二进制转ASCII）
   - 输入要转换的内容

### 文件结构
```
.
├── Ascbinary.py          # 主程序文件
├── locals.json           # 本地化字符串配置
├── ascii_char_to_binary.json  # ASCII-二进制映射表
└── README.md             # 项目说明文档
```

### 依赖项
- Python 3.x
- 标准JSON库（Python内置）

### 许可证
本项目采用MIT许可证。详见LICENSE文件。

---

<a name="english"></a>
## English Description

### Project Introduction
A simple Python tool for converting between ASCII characters and their binary representations. Features bilingual interface in Chinese and English.

### Features
- ASCII text to binary conversion
- Binary to ASCII text conversion
- Bilingual interface (Chinese/English)
- JSON-based localization system

### Usage
1. Ensure Python 3.x is installed
2. Prepare required JSON configuration files:
   - `locals.json` - contains localized strings for the interface
   - `ascii_char_to_binary.json` - contains ASCII to binary mapping table
3. Run the program:
   ```bash
   python Ascbinary.py
   ```
4. Follow the prompts:
   - First select interface language (1-Chinese, 2-English)
   - Then select conversion mode (1-ASCII to binary, 2-Binary to ASCII)
   - Enter the content to convert

### File Structure
```
.
├── Ascbinary.py          # Main program file
├── locals.json           # Localization strings configuration
├── ascii_char_to_binary.json  # ASCII-binary mapping table
└── README.md             # Project documentation
```

### Dependencies
- Python 3.x
- Standard JSON library (built-in with Python)

### License
This project is licensed under the MIT License. See LICENSE file for details.
