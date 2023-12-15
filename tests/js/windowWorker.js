console.log('[windowWorker] ~> init');
            
const windowWorker = () => {
    console.log('[windowWorker] ~> tick');

    var data = {
        'isPlaying'     : document.querySelector(".playControl").className.includes('playing') ? true : false,
        'cover'         : document.querySelector(".sc-artwork-4x").style.backgroundImage.slice(4, -1).replace(/"/g, "").replaceAll("50", "500"),
        'author'        : document.querySelector(".playbackSoundBadge__lightLink").innerHTML,
        'title'         : document.querySelector(".playbackSoundBadge__titleLink > span:nth-child(2)").innerHTML,
        'url'           : document.querySelector(".playbackSoundBadge__titleLink").href
    }

    // work harder not smarter :D

    let currentTime = document.querySelector(".playbackTimeline__timePassed > span:nth-child(2)").innerHTML.split(":");
    let duration = document.querySelector(".playbackTimeline__duration > span:nth-child(2)").innerHTML.split(":");

    data['currentTime'] = {
        'minutes' : parseInt(currentTime[0]),
        'seconds' : parseInt(currentTime[1])
    };

    data['duration'] = {
        'minutes' : parseInt(duration[0]),
        'seconds' : parseInt(duration[1])
    };

    data['duration']['minutes'] = data['duration']['minutes'] - data['currentTime']['minutes'];
    data['duration']['seconds'] = data['duration']['seconds'] - data['currentTime']['seconds'];

    data['currentTime']['minutes'] = 0;
    data['currentTime']['seconds'] = 0;

    window.pywebview.api.setData(data);

};

setInterval(windowWorker, 1000);