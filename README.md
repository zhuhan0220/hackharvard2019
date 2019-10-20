# hackharvard2019
## Inspiration
In modern society, people tend to be atomized into individual dots, keeping polite distance from others. Visually impaired people, whose mobility and possible activities are inevitablly restricted. However, there are volunteers who are motivated to help them live a normal life just as are, by offering their help both over the internet and in person. We are creating a platform connecting atomized individuals, helping visually impeded people live up to their independent lives with dignity. 

![ ](https://vthumb.ykimg.com/054106015C54157F000001410E053FB0)

## What it does
![](figs/vhelp.PNG)

Vhelp is a non-profit organization with a large cohert of visually impeded users and volunteers willing to offer assistance in their spare time. Vhelp currently needs a proprietary platform for visually impaired people to seek assistance from nearby volunteers. Volunteers can either call in via the camera at the user's hand, or come in person depending on the concrete situations, to solve various problems run into by users.

## Challenges we ran into
- Andriod app development, for both user and volunteers, possibly need to be able to support IOT devices and wearable devices
- Visually impaired users interact with mobile apps differently, we need voice input and recognition backends
- For in-person assist request, we need an algorithm to fetch the best match volunteer in terms of the nearest volunteer that can reach the user, and provide navigation services to him/her 
- Get GPS positions of users and match volunteers to users
- Providing navigation for volunteers to commute to the user's place
- (Optional feature) monitoring the interaction procedure to reduce risk, using sentimental analysis to issue 
- Review section

## Accomplishments that we're proud of
- [ ] We used Google position services API to grab real-time precise position data of the users and volunteers 
- [ ] We used Google speech-to-text API to tackle Audio input problem
- [ ] Used Andriod positioning service to grab the position of users
- [ ] Used firebase to receive updates of user positions, for the Google Cloud backend to perform matching later on
- [ ] Provide navigation service to volunteers, facilitate them finding the users
- [ ] Use real-time sentiment analysis to monitor potential 

Converting oral instructions of visually impeded users' into text for better communication 

## What we learned
- [ ] To use multiple Google Cloud APIs, like speech-to-text APIs, sentiment analysis APIs, Google APP Engine, Firebase etc. 
- [ ] To 

## What's next for myproj
