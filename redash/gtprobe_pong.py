"""Pong side of the probe helpers."""

from redash import gtprobe_ping


def pong(depth=0):
    return "pong" if depth <= 0 else gtprobe_ping.ping(depth - 1)
