content = {
    'hard_skills':
        [
            {'title': 'Python', 'url_name': 'python', 'link': 'https://www.python.org/'},
            {'title': 'Web Frameworks', 'url_name': 'web_frameworks', 'link': 'web_frameworks'},
            {'title': 'Databases', 'url_name': 'data', 'link': 'data'},
            {'title': 'ORM', 'url_name': 'orm', 'link': '#'},
            {'title': 'Web Servers', 'url_name': 'webserver', 'link': '#'},
            {'title': 'HTML5 & CSS3', 'url_name': 'htmlcss', 'link': '#'},
            {'title': 'JS', 'url_name': 'js', 'link': '#'},
            {'title': 'Git', 'url_name': 'git', 'link': 'https://git-scm.com/'},
            {'title': 'Docker', 'url_name': 'docker', 'link': 'https://www.docker.com/'}
        ],
    'necessary_useful':
        [
            {'title': 'IDE & Text redactors', 'url_name': 'ide'},
            {'title': 'Virtual Box', 'url_name': 'https://www.virtualbox.org/'},
            {'title': 'Ubuntu Linux', 'url_name': 'https://ubuntu.com/'},
            {'title': 'WakaTime', 'url_name': 'https://wakatime.com/'},
            {'title': 'GitHub', 'url_name': 'https://github.com/'},
            {'title': 'Platforms for online learning', 'url_name': 'ide'}

        ],
    'ide':
        [
            {'name': 'PyCharm', 'image': 'portfolio/dropmenu/ides/pycharm.png', 'url': 'https://www.jetbrains.com/pycharm/', 'rating': ['5', ' 5/5'], 'description': 'PyCharm is a cross-platform integrated development environment for the Python programming language. This IDE has a large set of tools for easy development in Python and its frameworks.'},
            {'name': 'Visual Studio Code', 'image': 'portfolio/dropmenu/ides/vc-code.png', 'url': 'https://code.visualstudio.com/', 'rating': ['4', ' 4.5/5'], 'description': 'Visual Studio Code is Microsoft\'s source code editor for Windows, Linux and macOS. It is a relatively "light" code editor for cross-platform web development.'},
            {'name': 'Sublime Text', 'image': 'portfolio/dropmenu/ides/sublime.png', 'url': 'https://www.sublimetext.com/', 'rating': ['4', ' 4.3/5'], 'description': 'Sublime Text is a cross-platform text editor for writing software code in various programming languages. It supports plug-ins in Python programming language.'},
            {'name': 'Spyder', 'image': 'portfolio/dropmenu/ides/spyder.png', 'url': 'https://www.spyder-ide.org/', 'rating': ['4', ' 4/5'], 'description': 'Spyder is a cross-platform interactive open source IDE. Very well suited for complex Python calculations, as out of the box it has advanced analysis, debugging, editing and profiling capabilities with data exploration.'},
            {'name': 'Emacs', 'image': 'portfolio/dropmenu/ides/emacs.jpg', 'url': 'https://www.gnu.org/software/emacs/download.html', 'rating': ['4', ' 4/5'], 'description': 'Emacs is one of the most popular text editors among developers and other technical professionals because of its extensibility and ability to perform a wide range of tasks, including editing text, writing code, organizing files, and navigating the Internet. Emacs is the favorite text editor of Guido van Rossum (the creator of Python). '}
        ],
    'web_frameworks':
        [
            {'name': 'Django', 'image': 'portfolio/dropmenu/web/django.png', 'url': 'https://www.djangoproject.com/', 'rating': ['9', ' 9/10'], 'description': 'Django is a free and open source web development framework for the Python programming language. It provides a set of tools and libraries for building web applications, facilitating development, database management, URL handling, authentication and more. Django follows DRY (Don\'t Repeat Yourself) principles and provides high performance and security. This framework is often used to build websites, social networks, e-commerce shops and other web applications.'},
            {'name': 'Flask', 'image': 'portfolio/dropmenu/web/flask.png', 'url': 'https://flask.palletsprojects.com/en/3.0.x/', 'rating': ['6', ' 6/10'], 'description': 'Flask is a minimalistic framework for Python web development. It provides a basic set of tools for building web applications, allowing developers to organise their code in a flexible way. Flask is easy to use and very flexible. In other words, developers can extend the functionality of Flask by adding third-party libraries and plugins as needed.'},
            {'name': 'FastAPI', 'image': 'portfolio/dropmenu/web/fastapi.png', 'url': 'https://fastapi.tiangolo.com/', 'rating': ['8', ' 8/10'], 'description': 'FastAPI is a modern and fast framework for building Python web applications and APIs that supports asynchronous programming and automatic documentation generation. It allows you to quickly create web services and APIs while ensuring security and reliability.'},
            {'name': 'Pyramid', 'image': 'portfolio/dropmenu/web/pyramid.png', 'url': 'https://trypyramid.com/', 'rating': ['6', ' 6/10'], 'description': 'Pyramid is a web development framework in the Python programming language that provides maximum flexibility and freedom to the developer. It provides basic tools and allows developers to select components and libraries as they see fit, making it suitable for developing a variety of web applications, from small websites to large systems.'},
            {'name': 'Tornado', 'image': 'portfolio/dropmenu/web/tornado.png', 'url': 'https://www.tornadoweb.org/en/stable/', 'rating': ['7', ' 7/10'], 'description': 'Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.'},


        ],
    'data':
        [
            {'name': 'PostgreSQL', 'image': 'portfolio/dropmenu/data/postgresql.png', 'url': 'https://www.postgresql.org/', 'rating': ['9', ' 9/10'], 'description': 'PostgreSQL is a powerful and open source relational database management system (RDBMS) that offers advanced features for storing and processing data. It supports multiple data types, multi-threading, transactions, indexes, and many other features.'},
            {'name': 'MySQL', 'image': 'portfolio/dropmenu/data/mysql.png', 'url': 'https://www.mysql.com/', 'rating': ['7', ' 7/10'], 'description': 'MySQL is a popular relational database management system (RDBMS) that provides efficient storage, management and access to data. It supports many applications and programming languages, and is highly performant and reliable. MySQL is open source and is widely used in web development and other areas for data storage.'},
            {'name': 'SQLite', 'image': 'portfolio/dropmenu/data/sqlite.png', 'url': 'https://www.sqlite.org/index.html', 'rating': ['6', ' 6/10'], 'description': 'SQLite is an embedded relational database management system (RDBMS) that stores data in one compact file. It is lightweight, fast and does not require a separate server, making it an ideal choice for embedded systems, mobile applications and small web applications. SQLite supports most of the SQL standard and provides a set of powerful features including transactions, indexes, and its own SQL query language. Translated with www.DeepL.com/Translator (free version)'},
            {'name': 'MongoDB', 'image': 'portfolio/dropmenu/data/mongodb.png', 'url': 'https://www.mongodb.com/', 'rating': ['6', ' 7/10'], 'description': 'MongoDB is a popular document-oriented non-relational database management system (NoSQL). It is designed to store and process data in BSON (binary JSON) format, which makes it flexible and scalable. MongoDB allows you to store data as JSON-like documents, which simplifies working with different types of data. Key features of MongoDB include horizontal scalability, data replication for fault tolerance, indexing for fast search, and a powerful query language. This DBMS is often used in web applications, analytical systems, and other applications where data may be unstructured or volatile.'},
        ],
    'certificates':
        [
            {
                'url': 'https://testprovider.com/ru/search-certificate/tp94083226',
                'image': 'portfolio/about/eng.png',
                'alt': 'Englishdom certificate It english',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP49180716',
                'image': 'portfolio/about/business_eng.jpg',
                'alt': 'Englishdom certificate Business english',
            },
            {
                'url': '',
                'image': 'portfolio/about/eng2.png',
                'alt': 'btc certificate it-eng',
            },
            {
                'url': 'https://certs.prometheus.org.ua/downloads/a6b4413491f444b99604fb1dcea69959/Certificate.pdf',
                'image': 'portfolio/about/git_cert.png',
                'alt': 'Prometheus certificate Git',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/tp66859821',
                'image': 'portfolio/about/git_itvdn.png',
                'alt': 'ITVDN certificate Git Basic',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP68005796',
                'image': 'portfolio/about/linux_itvdn.png',
                'alt': 'ITVDN certificate Linux administration basics',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP61356911',
                'image': 'portfolio/about/html_css_itvdn.png',
                'alt': 'ITVDN certificate HTML5 CSS3 Starter',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP17604341',
                'image': 'portfolio/about/java_itvdn.png',
                'alt': 'ITVDN certificate Java Basic',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP91289355',
                'image': 'portfolio/about/python_starter_itvdn.jpg',
                'alt': 'ITVDN certificate Python Starter',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP48073027',
                'image': 'portfolio/about/python_essential_itvdn.jpg',
                'alt': 'ITVDN certificate Python Essential',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP05300276',
                'image': 'portfolio/about/python_advanced_itvdn.png',
                'alt': 'ITVDN certificate Python Advanced',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP97444258',
                'image': 'portfolio/about/flask_itvdn.png',
                'alt': 'ITVDN certificate Flask',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP65257902',
                'image': 'portfolio/about/docker_itvdn.jpg',
                'alt': 'ITVDN certificate Docker',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP44626085',
                'image': 'portfolio/about/my_sql_itvdn.jpg',
                'alt': 'ITVDN certificate MySql',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP71870425',
                'image': 'portfolio/about/postgre_sql_itvdn.jpg',
                'alt': 'ITVDN certificate PostgreSQL',
            },
            {
                'url': 'https://testprovider.com/ru/search-certificate/TP05924985',
                'image': 'portfolio/about/django_starter_itvdn.jpg',
                'alt': 'ITVDN certificate Django starter',
            },
            {
                'url': 'https://stepik.org/cert/2020775',
                'image': 'portfolio/about/python_indie_course_stepic.jpg',
                'alt': 'Stepic certificate Python indie course',
            },
            {
                'url': 'https://stepik.org/cert/1803992',
                'image': 'portfolio/about/python_advanced_stepic.jpg',
                'alt': 'Stepic certificate Python advanced',
            },
            {
                'url': 'https://stepik.org/cert/1695951',
                'image': 'portfolio/about/python_balakirev.jpg',
                'alt': 'Stepic certificate Python Balakirev',
            },
            {
                'url': 'https://www.efset.org/cert/A9WsJv',
                'image': 'portfolio/about/EF_SET_eng.jpg',
                'alt': 'EF SET certificate',
            },
        ]
}


