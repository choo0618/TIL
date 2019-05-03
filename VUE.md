# VUE

## MVC(MTV)/ MVVM(vuejs)

|          MVC(MTV)          |      MVVM(vuejs)       |
| :------------------------: | :--------------------: |
|   `M` - Model(models.py)   |      `M` - Model       |
| `V` - View(Template.html)  |    `V` - View(HTML)    |
| `C` - Controller(views.py) | `VM` - View-Model(Vue) |



### django

```python
# 조건
{% if post.is_public %}
	{{ post }}
{% endif %}

# 반복
{% for post in posts %}
	{{ post }}
{% endfor %}
```



### VUE Directive

```python
<!-- 조건 -->
<p v-if="post.isPublic">
	{{ post }}
</p>

<!-- 반복 -->
<ul>
	<li v-for="post in posts">
    	{{ post }}
    </li>
</ul>
```











