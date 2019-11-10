all:	clean zip install

clean:
	unopkg remove ThemeChanger.oxt

zip:
	rm ThemeChanger.oxt
	zip -r ThemeChanger.oxt \
		description.xml \
		META-INF/manifest.xml \
		Addons.xcu \
		src/* \
		registration/* \
		description/*

install:
	unopkg add ThemeChanger.oxt