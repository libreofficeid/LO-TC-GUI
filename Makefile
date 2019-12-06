LO_PATH=/opt/libreofficedev6.4
LO_BIN=$(LO_PATH)/program
LO_UNOPKG=$(LO_BIN)/unopkg

all:	clean zip install


clean:
	$(LO_UNOPKG) remove ThemeChanger.oxt
	rm ThemeChanger.oxt

zip:
	zip -r ThemeChanger.oxt \
		description.xml \
		META-INF/manifest.xml \
		Addons.xcu \
		themechanger.py \
		lotc-modify-snap.sh \
		pythonpath/* \
		registration/* \
		description/*

install:
	$(LO_UNOPKG) add ThemeChanger.oxt
