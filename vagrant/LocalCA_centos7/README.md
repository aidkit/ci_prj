# AWS SAM @ CentOS7(vagrant)

## 概要
- vagrantにて作成されたCentOS7のVM環境に、AWS SAMを構築し、サンプルプログラムの動作確認をする。

### 環境(構築時の環境)
- Windows10 pro
- VirtualBox(5.2)
- Vagrant(2.2.4)

### ファイル構成

~~~
./
│  makeVm.bat		: 環境構築実行バッチ
│  README.md		：本ファイル
│  Vagrantfile		：vagrant定義ファイル
│
├─.vagrant			：Vagrant内部ファイル(基本触らない)
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
    └─ansible
        │  playbook.yml		：Ansible playBook
        │
        └─files
            config			:AWS CLI Configureファイル(ローカル環境向け)
~~~

### 使用方法
- 上記ディレクトリを任意の場所に配置し、makeVm.batをコマンドプロンプト上で実行！
### ※※※※※※SAMインストール※※※※※※※※
- 現在、原因不明でSAMがAnsibleで実行しているが、インストールされていない現象がある。
　makeVm.bat実行後、SSHで接続後、以下コマンドを実行し、SAMをインストールしてください。
	~~~
	$ pip install --user aws-sam-cli
	~~~
　

### SSHアクセス方法
‐ コマンドプロンプトでカレントフォルダ上で、「vagrant ssh」実行。

‐ ユーザ：vagrant　パス：vagrant　※vagrantユーザはSudo権限を付与されている。

~~~
vagrant@127.0.0.1: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).

上記エラー発生の場合は、「vagrant ssh-config」を実行し、IP、ポートを確認し
tera term等でアクセスする。
~~~

### SAM実行環境構築内容

- VM環境については、./vagrantfileを参照
	- 詳しい記載内容については、https://www.vagrantup.com/docs/vagrantfile/

- OS環境については、./shareDir/ansible/playbook.ymlを参照
	- 詳しい記載内容については、https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html

### SAM実行環境動作確認
- dockerの動作確認
	- 以下コマンドを実行し、Dockerが動作しているログを確認する。
	~~~
	$ docker run hello-world
	Unable to find image 'hello-world:latest' locally
	latest: Pulling from library/hello-world
	1b930d010525: Pull complete
	Digest: sha256:2557e3c07ed1e38f26e389462d03ed943586f744621577a99efb77324b0fe535
	Status: Downloaded newer image for hello-world:latest

	Hello from Docker!
	This message shows that your installation appears to be working correctly.

	To generate this message, Docker took the following steps:
	1. The Docker client contacted the Docker daemon.
	2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
		(amd64)
	3. The Docker daemon created a new container from that image which runs the
		executable that produces the output you are currently reading.
	4. The Docker daemon streamed that output to the Docker client, which sent it
		to your terminal.

	To try something more ambitious, you can run an Ubuntu container with:
	$ docker run -it ubuntu bash

	Share images, automate workflows, and more with a free Docker ID:
	https://hub.docker.com/

	For more examples and ideas, visit:
	https://docs.docker.com/get-started/
	~~~

- aws-sam-cliの動作確認
	- 以下コマンドを実行し、「Hello Wolrd」プロジェクトの実行が」できることを確認する。
		- testプロジェクトの作成
		~~~
		$ cd ~
		$ sam init --runtime python3.6 --name testpj
		~~~

		- API GatewayとLambdaを連携させる前提で、API Gatewayを通って流れてきたHTTPリクエストを模倣するイベントを作成する。
		~~~
		$ cd testpj
		$ sam local generate-event apigateway aws-proxy > ./event.json
		~~~

		- 実行
		~~~
		$ sam local invoke "HelloWorldFunction" -e event.json
		~~~
		※(初回実行時は、dockerコンテナイメージをインターネットからダウンロードしてくるので、少し時間がかかる。)

		- 以下出力を確認する。
		~~~
		[vagrant@samDev testpj]$ sam local invoke "HelloWorldFunction" -e event.json
		2019-06-04 11:20:09 Invoking app.lambda_handler (python3.6)

		Fetching lambci/lambda:python3.6 Docker container image...
		(中略)
		{"statusCode": 200, "body": "{\"message\": \"hello world\"}"}
		~~~

