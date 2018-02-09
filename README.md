# Loki_bot
IRC/Twitch bot geared towards managing elements of a twitch stream with ease. Control events, give viewers access to relevant data, etc.

Reimagination of the RhyCerBot project in Python, with different featureset in mind:

## User-facing features:
- Create and modify *battle lists* based on a 'sign-up' command in chat. First in, first to play, with a set list size (at which 'sign-up's are no longer taken)
- Call KH's api to receive *frame data* of requested moves of Smash 4 characters

## Non user-facing features:
- Determine user's level of permissions, based on if they are a subscriber, owner, follower, or just viewer of the stream this bot is attached to
