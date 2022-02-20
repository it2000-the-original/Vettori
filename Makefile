venv/bin/activate: requirements.txt
	# Creating a virtua environment
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate
	# Run the application with the virtua environment
	./venv/bin/python3 source/Vettori.py

clean: venv/bin/activate
	rm -rf source/__pycache__
	rm -rf source/Dialogs/__pycache__
	rm -rf venv

install: venv/bin/activate
	mkdir /usr/share/Vettori
	sudo cp -rf bin /usr/share/Vettori
	sudo cp -rf source /usr/share/Vettori
	sudo cp -rf venv /usr/share/Vettori
	sudo ln -s /usr/share/Vettori/bin/vettori /usr/bin/vettori
	sudo cp -rf icons /usr/share
	sudo gtk-update-icon-cache -f /usr/share/icons/hicolor/
	sudo cp -rf mime /usr/share
	sudo update-mime-database /usr/share/mime
	sudo cp -rf vettori.desktop /usr/share/applications
	sudo update-desktop-database /usr/share/applications

uninstall:
	sudo rm -rf /usr/share/Vettori
	sudo rm -f /usr/bin/vettori
	sudo rm -f /usr/share/icons/hicolor/16x16/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/22x22/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/24x24/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/32x32/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/36x36/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/48x48/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/64x64/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/72x72/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/96x96/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/128x128/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/192x192/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/256x256/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/512x512/apps/vettori.png
	sudo rm -f /usr/share/icons/hicolor/scalable/apps/vettori.svg
	sudo rm -rf /usr/share/applications/vettori.desktop
	sudo rm -f /usr/share/mime/packages/vettori.xml
	sudo update-mime-database /usr/share/mime
	sudo gtk-update-icon-cache -f /usr/share/icons/hicolor/
	sudo update-desktop-database /usr/share/applications
