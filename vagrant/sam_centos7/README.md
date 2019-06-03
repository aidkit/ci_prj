AWS SAM @ CentOS7(vagrant)

## 概要
- vagrantにて作成されたCentOS7のVM環境に、AWS SAMをインストールする。

### 必要環境
‐ Windows10 pro
- VirtualBox
- Vagrant

### ファイル構成

~~~
./
│  makeVm.bat		: インストール実行バッチ
│  README.md		：本ファイル
│  Vagrantfile		：vagrantファイル
│
├─.vagrant			：Vagrant内部ファイル
│  ├─machines
│  │  └─samDev
│  │      └─virtualbox
│  │              action_provision
│  │              action_set_name
│  │              box_meta
│  │              creator_uid
│  │              id
│  │              index_uuid
│  │              private_key	：vagrantユーザ　sshキー
│  │              synced_folders
│  │              vagrant_cwd
│  │
│  └─rgloader
│          loader.rb
│
└─shareDir
        playbook.yml	：Ansible PlayBook
~~~

### 使用方法
‐ makeVm.batをコマンドプロンプト上で実行！

### SSHアクセス方法
‐ コマンドプロンプトでカレントフォルダ上で、「vagrant ssh」実行。
	‐ ユーザ：vagrant　パス：vagrant

~~~
vagrant@127.0.0.1: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).

上記エラーの場合は、「vagrant ssh-config」を実行し、IP、ポートを確認し
tera term等でアクセスする。
~~~