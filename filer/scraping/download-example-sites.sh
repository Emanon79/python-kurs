example_dir=./example-sites
mkdir -p $example_dir

webpages=("http://www.scrapethissite.com/pages/simple/"
	  "http://www.scrapethissite.com/pages/forms/"
	  "http://books.toscrape.com/"
	  "http://quotes.toscrape.com/")

i=1
for webpage in "${webpages[@]}"; do
    wget --user-agent="Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0" $webpage -O "$example_dir/example_$i.html"
    i=$((i+1))
done

	  
