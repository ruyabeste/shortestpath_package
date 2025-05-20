.. Shortest Path Documentation documentation master file, created by
   sphinx-quickstart on Tue May 20 23:20:25 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Shortest Path Python Package
============================

.. contents::
   :depth: 2
   :local:
   :class: clean-toc

Welcome! This Python package provides a function to calculate the shortest 
(great-circle) distance between two geographical coordinates using the **Haversine formula**.

It is useful for geospatial tasks, navigation systems, travel estimations, and 
educational purposes. The package is lightweight and dependency-free.

---

Installation
============

Install from TestPyPI:

.. code-block:: bash

    pip install -i https://test.pypi.org/simple shortestpath12345678

Or clone from GitHub and install locally:

.. code-block:: bash

    git clone https://github.com/yourusername/shortestpath_project.git
    cd shortestpath_project
    pip install .

---

Usage Example
=============

Here's how you can use the package in your Python code:

.. code-block:: python

    from shortest_path.shortestpath import haversine

    # Paris (48.8566, 2.3522) to London (51.5074, -0.1278)
    distance = haversine(48.8566, 2.3522, 51.5074, -0.1278)
    print(f"Distance: {distance:.2f} km")

Expected Output:

.. code-block::

    Distance: 343.38 km

---

Function Explanation
====================

.. code-block:: python

    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculates the great-circle distance between two points using the Haversine formula.

        Parameters:
            lat1 (float): Latitude of point 1
            lon1 (float): Longitude of point 1
            lat2 (float): Latitude of point 2
            lon2 (float): Longitude of point 2

        Returns:
            float: Distance in kilometers
        """
        # Function body...

- Converts degrees to radians
- Applies the Haversine formula
- Returns the result in kilometers

---

License
=======

MIT License

You are free to use, modify, and distribute this package.

---

Contribution
============

Contributions are welcome! If you have suggestions, bug reports, or feature requests:

- Open an issue on GitHub
- Submit a pull request
- Or just say hi :)

---

Roadmap
=======

- [x] Add Haversine formula
- [ ] Add geodesic/Vincenty support
- [ ] Accept location input from JSON or tuple


