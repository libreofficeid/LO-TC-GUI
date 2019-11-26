all:	clean zip install

clean:
	unopkg remove ThemeChanger.oxt
	rm ThemeChanger.oxt

zip:
	zip -r ThemeChanger.oxt \
		description.xml \
		META-INF/manifest.xml \
		Addons.xcu \
		themechanger.py \
		pythonpath/* \
		registration/* \
		description/*

install:
	unopkg add ThemeChanger.oxt

# PATH=/Applications/LibreOffice.app/Contents/MacOS/:$PATH