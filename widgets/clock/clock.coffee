class Dashing.Clock extends Dashing.Widget

  ready: ->
    setInterval(@startTime, 500)

  startTime: =>
    now = today = new Date()

    h = (today.getHours() % 13) + 1
    m = today.getMinutes()
    s = today.getSeconds()
    m = @formatTime(m)
    s = @formatTime(s)
    @set('time', h + ":" + m + ":" + s)
    @set('date', now.getFullYear()+'/'+now.getMonth()+1+'/'+now.getDay())

  formatTime: (i) ->
    if i < 10 then "0" + i else i
