
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Youtube crawler server</h3>

  <p align="center">
    Backend side app: https://github.com/DenisLebedinsky/crawler-client 
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

	Youtube crawler is an app for CRUD data from Youtube.com to database
 
	Deployed on Heroku: https://scrapy-youtube.herokuapp.com/
	Client: https://github.com/DenisLebedinsky/crawler-client


### Built With

* [Puthon](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Pymongo](https://api.mongodb.com/python/current/)
* [MongoDB](https://www.mlab.com/)



<!-- GETTING STARTED -->
## Getting Started


To get a local copy up and running follow steps below.


### Prerequisites

	You need to install the following:

```sh
pip 19.0.2
Python 3.7.3
MongoDB 
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/DenisLebedinsky/crawler-server.git
```
2. Install pip packages
```sh
pip3 install -r requirements.txt
```
3. Set env 
```sh
VIRTUAL_ENV = <production>|<development>|<test> 
HOST = <your host>
PORT = <your port>
MONGODB_URI = <URI MongoDB>
```



<!-- USAGE EXAMPLES -->
## Usage

Run client ([https://github.com/DenisLebedinsky/crawler-client]) and it will communicate with this app



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Denis Lebedinsky - (denis.lebedinsky@intspirit.com) - denis.lebedinsky@intspirit.com

Project Link: [https://github.com/DenisLebedinsky](https://github.com/DenisLebedinsky)
