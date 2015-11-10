# MerakiCaptivePortal
Captive portal sample application written using Python / GAE

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## References
I used the click-through authorization method, described on the Meraki's documentation.

## Solution Overview

The solution is composed by two modules:

### Splash Page

Web application written using Python and hosted on GAE. It has one authentication screen and an authorization mechanism:

![](https://github.com/felipecembranelli/MerakiCaptivePortal/blob/master/Screenshots/tela1.PNG)

![](https://github.com/felipecembranelli/MerakiCaptivePortal/blob/master/Screenshots/tela2.PNG)

![](https://github.com/felipecembranelli/MerakiCaptivePortal/blob/master/Screenshots/python1.PNG)

Source-code: https://github.com/felipecembranelli/MerakiCaptivePortal/tree/master/Splash

### Admin Portal

Admin web application written using Python and hosted on GAE. It shows the Meraki's authorized users:

![](https://github.com/felipecembranelli/MerakiCaptivePortal/blob/master/Screenshots/admin.PNG)

Fonte: https://github.com/felipecembranelli/MerakiCaptivePortal/tree/master/Admin


## Credits
Felipe Cembranelli

## License
Free to use





