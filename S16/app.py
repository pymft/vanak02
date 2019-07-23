from flask import Flask, render_template

#
app = Flask("my app")


@app.route('/')
@app.route('/<int:rows>/<int:cols>')
def index(rows=100, cols=100):
    return render_template("index.html", rows=rows, cols=cols)

@app.route('/test')
def test():
    lst = [('Allah', 'Beneficent'), ('Merciful', 'Generous'), ('Sovereign', 'Master'), ('Holy', 'Peace'), ('Source of security', 'Loving Protector'), ('Glorious', 'Dominant Helper'), ('Creator', 'Maker'), ('Fashioner', 'Pre-ordainer'), ('Guide', 'Ever-Living'), ('Liberal', 'to Whom return all repentant'), ('Liberator', 'Comforter'), ('Chief', 'Liege-Lord'), ('Near', 'Preserver'), ('Originator', 'Resurrector'), ('Praiseworthy', 'Glorified'), ('Eternal', 'Mighty'), ('Very Forgiving', 'Appreciator'), ('Ever-present', 'Witness'), ('Compassionate', 'Kind'), ('Causer', 'Lord-possessor'), ('Vivifying', 'Annihilator'), ('Loving', 'Helping Friend'), ('Companion', 'Familiar'), ('Magnificent', 'Elegant'), ('All-knowing', 'All-seeing'), ('Benevolent', 'Possessor of fortune'), ('Adored', 'Ever-Existing'), ('Forgiver', 'Subduer'), ('Rememberable', 'Thank-worthy'), ('Liberal Bestower', 'Whom everything returns to'), ('Pure Beauty', 'Majesty'), ('Ever-foremost', 'Giver of Livelihood'), ('Truthful', 'Splitter'), ('Hearer', 'Quick'), ('Sublime', 'Original Inventor'), ('Perpetrator', 'Most High'), ('Judge', 'Consenting'), ('Conqueror', 'Pure'), ('All-Knowing', 'Ruler'), ('Ever-Lasting', 'Ever-enduring'), ('Defended', 'Distributer'), ('Independent', 'Enricher'), ('True to His word', 'Strong'), ('Self-sufficient', 'Effective Restorer of health'), ('Leader', 'Conclusion'), ('First', 'Eternal Last'), ('Evident', 'Hidden'), ('Hope', 'Who is invoked'), ('Lord of Favors', 'Lord of Bounties'), ('Ever-Alive', 'Ever-Durable'), ('One', 'Unique'), ('Chief', 'Self-Subsisting'), ('Able to do (Everything)', 'Great'), ('Governor', 'Exalted'), ('Most High', 'Supreme'), ('Friend', 'Master'), ('Resolute', 'Foremost Creator'), ('Mortifying', 'Deliverer'), ('Who throws down', 'Gatherer'), ('Who does Honor', 'Subduer'), ('Guardian', 'Defending Administrator'), ('Capable Power', 'Impenetrable'), ('Wise', 'Forbearing'), ('Authority', 'All-wise'), ('Liberal Giver', 'Preventer'), ('Who brings about distress', 'Who allows gains'), ('Who comes to help', 'Reckoner'), ('Just', 'Distinguisher'), ('Subtle', 'Noble'), ('Lord', 'Truth'), ('Splendid', 'Author'), ('Granter of amnesty', 'Avenger'), ('Bountiful', 'Plentiful'), ('Clement', 'Affectionate'), ('Alone', 'Single'), ('Over-Seer ', 'Who surrounds everything'), ('Protecting Advocate', 'Justice'), ('Manifest', 'Persevering'), ('Benign', 'Beloved One'), ('Who guides on the right path', 'Who leads on to the true path'), ('Light', 'Illuminator'), ('Ally', 'Helper'), ('Patient', 'Enduring'), ('Who takes away', 'Who brings about'), ('Glorious ', 'Requiter'), ('Who gives help', 'Who is called for help'), ('Splitter', 'Ever-Present')]
    return render_template("sample.html", verses=lst)

app.run(port=8080)
