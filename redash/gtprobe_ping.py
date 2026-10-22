"""Ping side of the probe helpers."""

from redash import gtprobe_pong


def ping(depth=0):
    return "ping" if depth <= 0 else gtprobe_pong.pong(depth - 1)
