headline = "Allir flokkar"
submenus = [
    {
        'icon':'movie',
        'image': 'https://d38kdhuogyllre.cloudfront.net/fit-in/2048x/filters:quality(65)/hd_posters/9dtrm0-6a17m8.jpg',
        "label": "Hvolpasveitin",
        "data": {
            "type": "pages",               
            "template": {            
                "type": "separate",
                "layout": "0,0,2,4",
                "icon": "msx-white-soft:movie",
                "color": "msx-glass"                    
            },
            "items": [
                {
                    "title": "Hvolpasveitin (4 af 4)",
                    "action": "video:https://ruv-vod.akamaized.net/lokad/5292295T0/5292295T0.m3u8",
                    "image": "https://d38kdhuogyllre.cloudfront.net/fit-in/2048x/filters:quality(65)/hd_posters/9dtrmh-89066o.jpg"
                }
            ]
        }
    },
]

{
    "headline": headline,
    "menu": [{
        "icon": "movie",
        "image": "https://d38kdhuogyllre.cloudfront.net/fit-in/2048x/filters:quality(65)/hd_posters/9dtrm0-6a17m8.jpg",
        "label": "Hvolpasveitin",
        "data": {
            "type": "pages",               
            "template": {            
                "type": "separate",
                "layout": "0,0,2,4",
                "icon": "msx-white-soft:movie",
                "color": "msx-glass"                    
            },
            "items": [
                
        {
            "title": "Hvolpasveitin (4 af 4)",
            "action": "video:https://ruv-vod.akamaized.net/lokad/5292295T0/5292295T0.m3u8",
            "image": "https://d38kdhuogyllre.cloudfront.net/fit-in/2048x/filters:quality(65)/hd_posters/9dtrmh-89066o.jpg"
        }
            ]
        }
    },
     {
            "icon": "movie",
            "label": "Youtube",
            "data": {
                "type": "pages",               
                "template": {                  
                    "type": "separate",
                    "layout": "0,0,2,4",
                    "color": "msx-glass"                    
                },
                "items": [{
                        "title": "testa youtube",                        
                        "action": "video:plugin:http://msx.benzac.de/plugins/youtube.html?id=sC46642qqHE",
                        "image": "https://img.youtube.com/vi/sC46642qqHE/0.jpg"
                    }, {
                        "title": "Video 4",                       
                        "action": "video:http://msx.benzac.de/media/video3.mp4",
                        "icon": "msx-white-soft:movie"
                    }, {
                        "title": "Video 3",                       
                        "action": "video:http://msx.benzac.de/media/video3.mp4",
                        "icon": "msx-white-soft:movie"
                    }, {
                        "title": "Testa yo",
                        "action": "video:https://ruv-vod.akamaized.net/opid/5224944T0/5224944T0.m3u8",
                        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/1200px-OSIRIS_Mars_true_color.jpg"
                    }]
            }
        }, {
            "icon": "music-note",
            "label": "My Example Audios",
            "data": {
                "type": "pages",
                "template": {                   
                    "type": "separate",
                    "layout": "0,0,2,3",
                    "icon": "msx-white-soft:music-note",
                    "color": "msx-glass"
                },
                "items": [{
                        "title": "Audio 1",
                        "action": "audio:http://msx.benzac.de/media/audio1.mp3"
                    }, {
                        "title": "Audio 2",                          
                        "action": "audio:http://msx.benzac.de/media/audio2.mp3"
                    }, {
                        "title": "Audio 3",
                        "action": "audio:http://msx.benzac.de/media/audio3.mp3"
                    }]
            }
        }, {
            "icon": "image",
            "label": "My Example Images",
            "data": {
                "type": "pages",
                "template": {
                    "type": "default",
                    "layout": "0,0,3,2",
                    "color": "msx-glass",
                    "imageFiller": "cover",
                    "action": "image:context"
                },
                "items": [{
                        "image": "http://msx.benzac.de/img/bg1.jpg"                      
                    }, {
                        "image": "http://msx.benzac.de/img/bg2.jpg"                       
                    }, {
                        "image": "http://msx.benzac.de/img/bg3.jpg"                       
                    }]
            }
        }]
}

