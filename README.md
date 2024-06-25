<p align="center">
    <img width="192px" src="./docs/Logo/CY_Logo_Q2.png" >
</p>
<h1 align="center"><b>DemoProject</b></h1>

<p align="center">開發項目模版</p>
<p align="center">V 0.0.1</p>

<main style="text-align: center;">

</main>

## 快速部署
### docker
```bash
docker compose up -d
```

## 項目結構
```
demoptoject     // 項目文件夾
├── README.md   // 概述
├── .gitignore  // git 忽略文件
├── docker-compose.yml // Docker Compose 配置文件
├── _document   // 相關文檔
│   ├── changelog.md
│   └── roadmap.md
├── backend
│   ├── db_api_ninja       // DataBase API 
│   └── docker-compose.yml // BackEnd Docker Compose 配置文件
└── frontend
    └── docker-compose.yml // Frontend Docker Compose 配置文件
```

```
db_api_ninja     // 項目文件夾
├── db_api_ninja // 項目根目錄
│   ├── api
│   ├── db_api_ninja
│   ├── main.py
│   ├── manage.py
│   └── start.sh
└── dockerfile ` // Docker 配置文件
```

## 查閱更多
查看 [Change Log(更新日志)](_document/changelog.md)