# -*- coding: utf-8 -*-

from example_samplers import *
# from samplers import website_up

def run(app, xyzzy):
    samplers = [
        SynergySampler(xyzzy, 3),
        BuzzwordsSampler(xyzzy, 2), # 10
        ConvergenceSampler(xyzzy, 1),
        WebsiteUpSampler(xyzzy, 4),
        ZhihuTopicSampler(xyzzy, 5),
        CommentsSampler(xyzzy, 6),
        WdjDollSampler(xyzzy, 7),
        RandomCat(xyzzy, 5)
    ]

    try:
        app.run(debug=True,
                port=5000,
                threaded=True,
                use_reloader=False,
                use_debugger=True
                )
    finally:
        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"
