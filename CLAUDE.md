# 电商接口自动化测试框架

## 项目概述

基于 Python + pytest + Allure 的电商后台管理系统接口自动化测试框架。采用数据驱动模式，测试数据与测试代码分离，支持动态参数注入、全字段 JSON 断言、MySQL 数据库操作及 Allure 测试报告生成。

## 技术栈

| 技术 | 用途 |
|------|------|
| pytest | 测试框架 |
| requests | HTTP 接口请求 |
| Allure | 测试报告 |
| PyMySQL | MySQL 数据库操作 |
| YAML | 测试用例数据文件 |
| Jinja2 | 测试数据模板渲染 |
| Faker | 随机测试数据生成 |
| DeepDiff | JSON 深度对比断言 |
| openpyxl | Excel 文件读写 |
| yagmail | 邮件发送 |

## 项目结构

```
├── common/                    # 公共模块
│   ├── case_template.py       # YAML 用例模板生成
│   ├── debug.py               # 动态数据生成函数 (Faker/随机数/数据库查询)
│   ├── encryption.py          # 加密工具 (MD5, Base64)
│   ├── exchange_data.py       # 参数提取与变量池管理（已废弃）
│   ├── operator_yaml.py       # YAML 文件读写操作
│   ├── read_case_data.py      # 读取 YAML 测试用例数据（支持 Jinja2 渲染）
│   ├── read_excel.py          # Excel 文件读写
│   ├── read_file.py           # 配置文件读取
│   ├── setting.py             # 全局配置（数据库连接/环境/路径）
│   ├── write_case_result_data.py  # 接口返回结果写入 YAML
│   └── 邮件.py                # 压缩报告并发送邮件
├── config/                    # 配置文件
│   ├── config.yaml            # 邮件配置 + extra_pool 变量池
│   ├── environment.yaml       # 环境配置 (host/headers/Authorization)
│   └── read_environment.py    # 环境配置读取与 token 更新
├── datas/                     # 测试用例数据
│   ├── logon.yaml             # 登录接口用例
│   ├── excel/                 # Excel 数据与模板
│   ├── uesrquery/             # 用户管理模块用例
│   │   ├── add.yaml           # 添加用户用例
│   │   ├── query.yaml.yaml    # 查询用户用例
│   │   ├── queryid.yaml       # 按 ID 查询用例
│   │   └── queryid_sql.yaml   # SQL 插入后查询用例
│   └── sqlshuju/
│       └── query_sql.py       # SQL 语句定义（增删测试数据）
├── test_case/                 # 测试代码
│   ├── __init__.py            # 测试基类 Test (封装 SenApi)
│   ├── test_login.py          # 登录模块测试
│   └── uesr_control_test/
│       ├── adduesr_test.py    # 添加用户测试
│       └── query_test.py      # 查询用户测试
├── utils/                     # 工具模块
│   ├── asst.py                # 断言方法 (assert_tet / assert_diff)
│   ├── logutil.py             # 彩色日志（控制台 + 文件）
│   ├── mails.py               # SMTP 邮件发送
│   ├── mysqlutil.py           # MySQL 数据库操作封装
│   └── requestutil.py         # HTTP 请求封装 (SenApi)
├── log/                       # 运行日志输出
├── reports/                   # Allure 报告输出
├── conftest.py                # pytest 全局 fixture（自动登录获取 token）
├── pytest.ini                 # pytest 配置
├── run_all.py                 # 运行入口
└── requirements.txt           # 项目依赖
```

## 核心架构

### 数据驱动流程

```
YAML 用例文件 (datas/*.yaml)
    │  (Jinja2 模板渲染 + 函数注入)
    ▼
read_case_data.py
    │  (返回用例字典列表)
    ▼
pytest 参数化 → SenApi 发送请求 → 断言 (assert_tet / assert_diff)
```

### 测试数据 YAML 格式

```yaml
- case_name: 用例名称
  method: post                # 请求方法
  is_run: true                # 是否执行
  path: /api/private/v1/users # 接口路径
  data:                       # 请求参数
    username: {{get_name()}}  # 支持动态函数
    password: "123456"
  result:                     # 预期结果（断言）
    msg: 创建成功
```

### 动态数据函数

在 `common/debug.py` 中定义，可在 YAML 中以 `{{函数名()}}` 形式调用：
- `get_name()` — 随机中文姓名
- `get_phone()` — 随机手机号
- `get_email()` — 随机邮箱
- `get_random()` — 6位随机字母数字
- `get_response_text(res, key)` — 从 JSON 响应提取指定字段

## 运行方式

```bash
# 安装依赖
pip install -r requirements.txt

# 运行全部测试
python run_all.py

# 或使用 pytest 命令
pytest -s --alluredir=./temps --clean-alluredir

# 生成 Allure 报告
allure generate ./temps -o ./reports --clean
```

## 配置说明

### 环境配置 (`config/environment.yaml`)

支持 `test_environment` 和 `pre_environment` 两套环境。测试框架启动时 conftest.py 会自动登录并将 token 写入环境配置。

### 数据库配置 (`common/setting.py`)

```python
DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'api_server',
    'port': 3306,
    'charset': 'utf8'
}
```

## 测试模块

### 1. 登录模块 (`test_login.py`)
- 参数化读取 `datas/logon.yaml`
- 使用 `assert_diff` 进行全字段断言（排除 token 动态字段）
- 使用 `assert_tet` 对 msg 字段断言

### 2. 添加用户 (`adduesr_test.py`)
- 参数化读取 `datas/uesrquery/add.yaml`
- 使用 `{{get_name()}}` 等动态函数生成测试数据
- 测试后清理数据库插入的数据

### 3. 查询用户 (`query_test.py`)
- 多子模块：查询列表、按 ID 查询、SQL 插入后查询
- SQL 插入数据后查询验证，验证后清理

## 断言方法

- **`assert_tet(reality, expect)`** — 简单相等断言，用于单字段验证
- **`assert_diff(reality, expect, exclude_paths=[])`** — DeepDiff 深度对比，忽略指定路径（如 token），忽略字符串类型差异
- **`assert_diff_Ignore_case(reality, expect)`** — 忽略大小写的深度对比

## 日志

日志使用 `colorlog` 输出彩色日志到控制台，同时按日期写入 `log/` 目录。

## 邮件通知

运行完成后可将 Allure 报告压缩为 zip 包，通过 QQ 邮箱 SMTP 发送给指定收件人。邮件配置在 `config/config.yaml` 中。

## 注意事项

- 被测接口为 `http://127.0.0.1:8888`，需本地启动后台服务
- 数据库 `api_server` 需提前创建并包含对应表结构
- YAML 文件中 `is_run` 为 `false` 时跳过该用例
- 测试框架默认使用 `test_environment` 环境，可在 `setting.py` 中切换为 `pre_environment`
