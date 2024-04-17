AUTHOR = "Leo"
SITENAME = "Leo’s blog"
SITESUBTITLE = "A nook to hoard my manuscripts."
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = "Asia/Shanghai"
DEFAULT_LANG = "zh-CN"
DEFAULT_DATE_FORMAT = "%Y年 %b%d日"

ARTICLE_URL = "{category}/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
ARTICLE_SAVE_AS = "{category}/{date:%Y}-{date:%m}-{date:%d}-{slug}.html"
CATEGORY_URL = "category/{slug}.html"
PAGE_URL = "pages/{slug}.html"
TAG_URL = "tag/{slug}.html"
TAGS_URL = "/tags.html"
ARCHIVES_URL = "/archives.html"

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Umami statistic
# turn off umami when developing
UMAMI_STATISTIC = False
UMAMI_WEB_ID = "b508982a-f7bf-4c24-a948-8de93b0cb81d"

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 100

# 导出时不删除的文件
OUTPUT_RETENTION = [
    ".git",
    ".gitignore",
    "favicon.ico",
    "robots.txt",
    "map.html",
]

# md与jupyter两种布局
MARKUP = ("md", "ipynb")
IPYNB_MARKUP_USE_FIRST_CELL = True

PLUGIN_PATHS = ["plugins"]

from pelican_jupyter import markup as nb_markup

PLUGINS = [
    nb_markup,
    "pelican-toc",
    "render_math",
    "sitemap",
    "replacer",
    "neighbors",
    "pelican-bookshelf",
    "search",
]
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_SKIP_CSS = True

THEME = "themes/attila"
DIRECT_TEMPLATES = [
    "index",
    "authors",
    "categories",
    "tags",
    "archives",
    "about",
    "search",
]

HOME_COVER = (
    "https://api.onedrive.com/v1.0/shares/s!AtseC45rsRhNunLc0Y-tTns1SGA5/root/content"
)

HEADER_COVER = (
    "https://api.onedrive.com/v1.0/shares/s!AtseC45rsRhNwFfSnZ1Pc1osKbni/root/content"
)

COPYRIGHT_YEAR = 2024
SHOW_AUTHOR_BIO_IN_ARTICLE = True
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = False
SHOW_PAGES_ON_MENU = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = True
ALLOW_GOOGLE_FONTS = False

MENUITEMS = (
    ("Home", "/"),
    ("碎碎唸", "/category/sui-sui-nian.html"),
    ("故紙堆", "/category/gu-zhi-dui.html"),
    ("在路上", "/category/zai-lu-shang.html"),
    ("山牆邊", "/pages/shan-qiang-bian.html"),
    ("破櫥簏", "https://neodb.social/users/Leo/"),
    ("Archives", "/archives.html"),
    ("Tags", "/tags.html"),
    ("About", "/about.html"),
)

# Author info
AUTHOR_META = {
    "leo": {
        "name": "Leo",
        "cover": "https://api.onedrive.com/v1.0/shares/s!AtseC45rsRhN-QsM6F2bdOKv3Wrm/root/content",
        "image": "https://cravatar.cn/avatar/95e31f6808fafa1f8ef3313b6f0b10e6?s=800",
        "mastodon": {
            "title": "@leonis@dragon-fly.club",
            "url": "https://mast.dragon-fly.club/@leonis",
        },
        "github": "Tseing",
        "location": {
            "title": "Tientsin",
            "url": "https://www.bing.com/maps?cp=39.116572%7E117.361669&lvl=10.1",
        },
        "email": "im.yczeng@outlook.com",
        "rss": "/feed.xml",
        "bio": "A chemist who doesn’t know about classical literature isn’t a good programmer. Cool, huh?",
    }
}

CATEGORY_META = {
  '碎碎念': {
      'cover': 'https://api.onedrive.com/v1.0/shares/s!AtseC45rsRhN-ivC0GRPj-6Ef97d/root/content',
      'description': 'We can only see a short distance ahead, but we can see plenty there that needs to be done.'
  },
  '故纸堆': {
    'cover': 'https://api.onedrive.com/v1.0/shares/s!AtseC45rsRhN-iZngQ1TZL7H7jiv/root/content',
    'description': '溪柴火軟蠻氈暖，我與貍奴不出門。'
  },
  '在路上': {
      'cover': 'https://api.onedrive.com/v1.0/shares/s!AtseC45rsRhN-i28e3JFm3ec3wUY/root/content',
      'description': '無窮的遠方，無數的人們，都和我有關。'
  }
}

SOCIAL = (
    ("search", "/search.html"),
    ("foreverblog", "https://img.foreverblog.cn/wormhole_2_tp.gif"),
    ("travellings", "https://www.travellings.cn/assets/w.png"),
)

SHARE_MEDIA = (
    ("Share-link", "复制文章链接"),
    ("Mastodon", "嘟嘟到 Mastodon"),
    ("Weibo", "分享到微博"),
    ("Email", "通过 Email 转发"),
)

WALINE_COMMENT = {
    "serverURL": "https://waline-1-d9689975.deta.app/",
    "locale": {"placeholder": "欢迎评论，填写邮箱可以获取头像和收到回复通知～"},
}

# MathJax(3.2.0)
MATH_JAX = {
    "source": "'https://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/mathjax/3.2.0/es5/tex-mml-chtml.js'"
}

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.8, "pages": 0.5},
    "changefreqs": {"articles": "daily", "indexes": "daily", "pages": "monthly"},
    "exclude": ["tag/", "category/"],
}

# toc
TOC = {
    "TOC_HEADERS": "^h[2-3]",  # What headers should be included in
    # the generated toc
    # Expected format is a regular expression
    "TOC_RUN": "true",  # Default value for toc generation,
    # if it does not evaluate
    # to 'true' no toc will be generated
    "TOC_INCLUDE_TITLE": "false",  # If 'true' include title in toc
}

# pelican-search
STORK_INPUT_OPTIONS = {
    "html_selector": ".post-content",
    "exclude_html_selector": "script, pre, .toc-nav, .math",
    "minimum_index_ideographic_substring_length": 2,
}

STORK_OUTPUT_OPTIONS = {"excerpts_per_result": 1}

# code replace to
REPLACES = (
    (
        "{warn begin}",
        '<div class="warn-info"><p><span><i class="fa-solid fa-circle-exclamation"></i>&ensp;Warning</span>&emsp;',
    ),
    ("{warn end}", "</p></div>"),
    (
        "{note begin}",
        '<div class="note-info"><p><span><i class="fa-solid fa-note-sticky"></i>&ensp;Note</span>&emsp;',
    ),
    ("{note end}", "</p></div>"),
)

# import lightgallery
# markdown extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.md_in_html": {},
        "lightgallery": {},
        "markdown_link_attr_modifier": {
            "new_tab": "on",
            "no_referrer": "off",
            "auto_title": "off",
        },
    },
    "output_format": "html5",
}

CSS_OVERRIDE = [
    "theme/css/customize.css",
    "theme/css/plugins.css",
    "theme/css/lightgallery.min.css",
    "theme/css/bookshelf.css",
]

# bookshelf plugin
# BOOKSHELF = {
#     "INFOS": ["出版年", "页数", "定价", "ISBN"],
#     "SAVE_TO_MD": False,
#     "WAIT_TIME": 2,
# }
