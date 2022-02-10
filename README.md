# getlevels 

Get any Level of subdomains form `1...N`

## Installation

```bash
git clone https://github.com/0xdln1/getlevels
cd getlevels
chmod +x getlevels 
sudo mv getlevels /usr/local/bin
```

## Example Usage

```
📄 subdomains.txt
blog.intigriti.com
api.intigriti.com
click.intigriti.com
login.intigriti.com
go.intigriti.com
newsletter.intigriti.com
www.careers.intigriti.com

▶ cat subdomains.txt | getlevels 2
log.intigriti.com                                                                                                                               
api.intigriti.com                                                                                                                                
click.intigriti.com                                                                                                                              
login.intigriti.com                                                                                                                              
go.intigriti.com                                                                                                                                 
newsletter.intigriti.com

▶ cat files.txt | getlevels 3
www.careers.intigriti.com
```
