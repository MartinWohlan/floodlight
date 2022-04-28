import matplotlib

from floodlight.vis.utils import check_axes_given


@check_axes_given
def plot_positions(
    xy, frame: int, ball: bool, ax: matplotlib.axes, **kwargs
) -> matplotlib.axes:
    """
    Scatter plots positions for a given frame of the XY.xy array on a matplotlib.axes.

    Parameters
    ----------
    xy: floodlight.core.xy.XY
        Spatio-temporal data fragment object that contains the positions
        (XY.xy: np.ndarray) and functgiions for manipulation.
    frame: int
        Frame in the postions-array (XY.xy) for which the positions are plotted.
    ball: bool
        If set to False marker="o". Else marker="."
    ax: matplotlib.axes
        Axes from matplotlib library on which the positions are plotted.
    kwargs:
        Optional keyworded arguments e.g. {'color', 'zorder', 'marker'}
        which can be used for the plot functions from matplotlib. The kwargs are
        only passed to the plot functions of matplotlib.

    Returns
    -------
    matplotib.axes
        A matplotlib.axes on which the positions are plotted.
    """

    # kwargs which are used to configure the plot with default values.
    # All other kwargs are just getting passed to the scatter() method.
    marker = kwargs.pop("marker", "o" if not ball else ".")
    color = kwargs.pop("color", "black" if not ball else "grey")
    zorder = kwargs.pop("zorder", 1)

    # plotting the positions
    # if ball is false
    if not ball:
        ax.scatter(
            x=xy.x[frame],
            y=xy.y[frame],
            marker=marker,
            color=color,
            zorder=zorder,
            **kwargs,
        )
    # if ball is true
    elif ball:
        ax.scatter(
            x=xy.x[frame],
            y=xy.y[frame],
            marker=marker,
            color=color,
            zorder=zorder,
            **kwargs,
        )

    return ax


@check_axes_given
def plot_trajectories(
    xy,
    start_frame: int,
    end_frame: int,
    ball: bool,
    ax: matplotlib.axes,
    **kwargs,
) -> matplotlib.axes:
    """
    Draws the trajectories of the XY.xy array for a given range of frames on a
    matplotlib.axes.

    Parameters
    ----------
    xy: floodlight.core.xy.XY
        Spatio-temporal data fragment object that contains the positions
        (XY.xy: np.ndarray) and functions for manipulation.
    start_frame: int
        First frame of the range of frames for which the trajectories are drawn.
    end_frame: int
        Last frame of the range of frames for which the trajectories are drawn.
    ball: bool
        If set to False marker="o". Else marker="."
    ax: matplotlib.axes
        Axes from matplotlib library on which the trajectories are drawn.
    kwargs:
        Optional keyworded arguments e.g. {'linewidth', 'zorder', 'linestyle', 'alpha'}
        which can be used for the plot functions from matplotlib. The kwargs are only
        passed to all the plot functions of matplotlib.

    Returns
    -------
    matplotib.axes
        A matplotlib.axes on which the trajectories are drawn.
    """

    # kwargs which are used to configure the plot with default values.
    # All other kwargs are just getting passed to the plot() method.
    color = kwargs.pop("color", "black" if not ball else "grey")
    zorder = kwargs.pop("zorder", 1)
    # ball trajectories are thinner per default
    linewidth = kwargs.pop("linewidth", 1 if not ball else 0.5)

    # iterating over every object (for instance players) in the XY.xy array and plot the
    # trajectories for the given range of frames
    for i in range(0, len(xy.xy[0]), 2):  # TODO xy.N instead of len(xy.xy[0])

        x = xy.xy[start_frame:end_frame, i]
        y = xy.xy[start_frame:end_frame, i + 1]
        ax.plot(x, y, color=color, zorder=zorder, linewidth=linewidth, **kwargs)

    return ax
