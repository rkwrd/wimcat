# wimcat - Where is my container at?
## Setting up headless firefox in ubuntu
sudo apt-get install firefox


Setting up virtual X server
	sudo apt-get install xvfb
	sudo Xvfb :10 -ac

Headless Firefox
	export DISPLAY=:10
	firefox

