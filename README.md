
# Git 实践过程记录

---

### 学习资料来源及相关链接

- [人人都能看懂的Git教程](https://www.bilibili.com/video/BV1d6XVYqEuy)
- [给傻子的Git教程](https://www.bilibili.com/video/BV1Hkr7YYEh8)
- [git 官方文档](https://git-scm.com/docs)

---

### 实践流程

##### 从官网下载git的win64安装包并安装
- 初次使用git时，需要配置全局邮箱和用户名

>- 使用git config --global user.email "you@example.com"配置全局邮箱
>- 使用git config --global user.name "Your Name"配置全局用户名

##### 向远程仓库添加内容

>- 使用git init初始化本地仓库
>- 使用git remote add origin 仓库地址，添加远程仓库
>- 使用git add *将所有文件添加到本地仓库
>- 使用git commit -m "提交信息"将本地仓库内容提交到远程仓库
>- 使用git push将本地仓库内容推到远程仓库

---

### 每次提交的主要内容进行简要说明

1. 初始化本地仓库，首次添加readme.md文件
2. 首次更新文件内容
3. 第二次更新文件内容

---

### 遇到的问题及解决方法

没有问题，以前用过git

---

### Git学习心得

照着视频就够用了

### 进一步学习

>- git merge 分支合并
>- git branch 分支管理
>- git reset 回滚
>- git rebase 重基