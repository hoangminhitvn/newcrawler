```
Scrapy NewCrawler Project Readme
```

```
Create Environment run scrapy
```
Using virtualenv.\n
Install virtualenv: $pip install virtualenv\n
Create environment: $virtualenv env_linux (with env_linux is name virtualenv created in Linux machine)\n

```
Activate virtualenv
```
Activate virtualenv on Linux/Mac OS: $source env_linux/bin/activate\n
Activate virtualenv on Windows     : >. env_linux\Script\activate\n
Result after activate: (env_linux)$\n

```
Install Scrapy
```
Install scrapy on virtualenv: (env_linux)$pip install -r requirement.txt\n


```
Run Scrapy
```
Run scrapy: $scrapy crawl web -a config_fil=sources/config/<name_config_file> -o output/<name_output_file>\n
Example: $scrapy crawl web -a config_file=sources/config/baoboi_config.json -o output/baobao_output.json\n

```
Deactivate virtualenv
```
Deactivate virtualenv: $deactivate\n