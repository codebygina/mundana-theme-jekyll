source "https://rubygems.org"

# Specify Ruby version (set to 2.7 for compatibility with ruby_dep)
ruby '2.7.0'

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#

# If you have any plugins, put them here!
gem 'wdm', '>= 0.1.0' if Gem.win_platform?

# Update listen to a version compatible with Ruby 2.7
gem "listen", ">= 3.2.0"

# Update ruby_dep to a compatible version (1.5.0 is compatible with Ruby 2.7)
gem 'ruby_dep', '~> 1.5.0', require: false

# Jekyll plugins
group :jekyll_plugins do
    gem 'jekyll-feed'
    gem 'jekyll-sitemap'
    gem 'jekyll-paginate'
    gem 'jekyll-seo-tag'
end
