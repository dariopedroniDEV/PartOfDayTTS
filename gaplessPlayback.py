import pyglet
from pyglet.media import SourceGroup
# I swear, this shit is more complicated than Neon Genesis Evangelion
player = pyglet.media.Player()
source1 = pyglet.resource.media('music/wishloop.mp3')
source_group = SourceGroup()
source_group.add(source1)
player.queue(source_group)
player.loop = True
player.play()


pyglet.app.run()