
#music = pyglet.resource.media('music/wishloop.mp3', streaming=False)
#player = pyglet.media.Player()
#player.EOS_LOOP = 'loop'
#music.play()

# I swear, this shit is more complicated than Neon Genesis Evangelion
import pyglet
from pyglet.media import SourceGroup

source1 = pyglet.resource.media('music/wishloop.mp3')
source_group = SourceGroup()
source_group.add(source1)
player.queue(source_group)
pyglet.app.run()