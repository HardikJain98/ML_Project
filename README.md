### Steps for setting up a page in Ubuntu 22.04:
```
sudo apt install -y gem ruby ruby-bundler ruby-dev
sudo gem install jekyll jekyll-feed jekyll-gist jekyll-paginate jekyll-sass-converter jekyll-coffeescript github-pages
```

### Make changes to website and test it
```
bundle update && bundle exec jekyll serve --config "_config.yml,_config_dev.yml"
```

### Where to view the changes
```
http://localhost:4000
```

### References
* https://jekyllrb.com/docs/step-by-step/01-setup/
* https://stackoverflow.com/a/68399131
* https://github.com/just-the-docs/just-the-docs
* https://just-the-docs.github.io/just-the-docs/


### Steps for setting up page in Windows 10/11

* Follow the steps (1-4) in the below link - https://jekyllrb.com/docs/installation/windows/
* Jekyll is ready to use after this


### Make changes to website and test it (run the below command from inside the Project folder)
```
bundle update && bundle exec jekyll serve --config "_config.yml,_config_dev.yml"
```

### Where to view the changes
```
http://localhost:4000
```