from flask import Flask,render_template

app = Flask(__name__)
app.config.update({
    'TEMPLATES_AUTO_RELOAD': True
})

movies = [
        {
            'name':'中国机长1',
            'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating':7.3
        },
        {
            'name': '中国机长2',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长3',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name':'中国机长1',
            'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating':7.3
        },
        {
            'name': '中国机长2',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长3',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长1',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长2',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长3',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        }
    ]

tvs = [
        {
            'name':'中国机长1',
            'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating':7.3
        },
        {
            'name': '中国机长2',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长3',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name':'中国机长1',
            'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating':7.3
        },
        {
            'name': '中国机长2',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长3',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长1',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长2',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        },
        {
            'name': '中国机长3',
            'thumbnail': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568261402.webp',
            'rating': 7.3
        }
    ]
moudle_name={
    'movies': '电影',
    'tvs': '电视剧'
}
@app.route('/')
def index():
    context = {
        'movies': movies,
        'tvs': tvs
    }
    return render_template('index.html',**context)

@app.route('/list/<category>/')
def item_list(category):
    context = {
        'category': category,
        'mdl_name': moudle_name.get(category)
   }
    return render_template('list.html',** context)

if __name__ == '__main__':
    app.run(debug=True)
