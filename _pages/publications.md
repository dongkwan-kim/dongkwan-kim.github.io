---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if page.author and site.data.authors[page.author] %}
  {% assign author = site.data.authors[page.author] %}{% else %}{% assign author = site.author %}
{% endif %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% assign publication_groups = site.publications | sort: "type" | group_by: "type" %}
{% for publications in publication_groups %}
  <h2 class="archive__subtitle">{{publications.name | capitalize}}</h2>
  {% assign prefix = publications.name | slice: 0 | capitalize %}
  {% for post in publications.items reversed %}
    {% assign prefix_index = forloop.length | minus: forloop.index0 %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}
