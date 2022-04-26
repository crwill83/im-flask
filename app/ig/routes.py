from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required


ig = Blueprint('ig', __name__, template_folder='ig_templates')

from .forms import AddToCart, AddToolForm, CreatePostForm, EditToolForm, UpdatePostForm
from app.models import User, db, Inventory, Post, Rental, Cart

# Adding a cart page
@ig.route('/cart')
def cart(inventory_id):

    # cart = Cart.query.all()[::-1]
    cart_items = db.session.query(cart.inventory_id, inventory.inventory_id).all()

    return render_template('cart.html', cart_items=cart_items)

# Add item to cart
@ig.route('/add-cart/<int:tool_id>', methods=["GET", "POST"])
@login_required
def addToCart(tool_id):
    print('success')
    cart_item = Cart(current_user.id, tool_id)
    db.session.add(cart_item)
    db.session.commit()
    # if request.method == "POST":
    #     tool = Inventory.query.filter(Inventory.id == tool_id)
    #     form = Cart(tool=tool)

    #     db.session.add(form)
    #     db.session.commit()

    # form = AddToCart()
    # if request.method == "POST":
        



    return redirect(url_for('tools'))

    # return render_template('addtocart.html', form=form)
########

@ig.route('/posts')
def posts():
    posts = Post.query.all()[::-1]
    return render_template('posts.html', posts = posts)

#### added tools list page
@ig.route('/tools')
def tools():
    tools = Inventory.query.all()[::-1]
    return render_template('tools.html', tools = tools)

#### added add tool page
@ig.route('/add-tool', methods=["GET", "POST"])
@login_required
def addTool():
    form = AddToolForm()
    if request.method == "POST":
        if form.validate():
            item_name = form.item_name.data
            item_model = form.item_model.data
            item_serial = form.item_serial.data
            item_description = form.item_description.data
            item_image = form.item_image.data

            item = Inventory(item_name, item_model, item_serial, item_description, item_image, current_user.id)

            db.session.add(item)
            db.session.commit()

            return redirect(url_for('ig.tools'))

    return render_template('addtool.html', form = form)
#####
## individual tool page
@ig.route('/tools/<int:tool_id>')
def toolDetails(tool_id):
    tool = Inventory.query.filter_by(id=tool_id).first()
    if tool is None:
        return redirect(url_for('ig.tools'))
    return render_template('tooldetails.html', tool = tool)

####
# Edit tool function
@ig.route('/tools/update/<int:tool_id>', methods=["GET","POST"])
@login_required
def editTool(tool_id):
    tool = Inventory.query.filter_by(id=tool_id).first()
    if tool is None:
        return redirect(url_for('ig.tools'))
    if tool.user_id != current_user.id:
        return redirect(url_for('ig.tools'))
    form = EditToolForm()
    if request.method == "POST":
        if form.validate():
            item_name = form.item_name.data
            item_model = form.item_model.data
            item_serial = form.item_serial.data
            item_description = form.item_description.data
            item_image = form.item_image.data

            # update the original tool
            tool.item_name = item_name
            tool.item_model = item_model
            tool.item_serial = item_serial
            tool.item_description = item_description
            tool.item_image = item_image

            db.session.commit()

            return redirect(url_for('ig.tools'))         
    return render_template('updatetool.html', form=form, tool = tool)

#### Delete tool function

@ig.route('/tools/remove/<int:tool_id>', methods=["POST"])
@login_required
def removeTool(tool_id):
    tool = Inventory.query.filter_by(id=tool_id).first()
    if tool is None:
        return redirect(url_for('ig.tools'))
    if tool.user_id != current_user.id:
        return redirect(url_for('ig.tools'))

    db.session.delete(tool)
    db.session.commit()
               
    return redirect(url_for('ig.tools'))

####

@ig.route('/create-post', methods=["GET", "POST"])
@login_required
def createPost():
    form = CreatePostForm()
    if request.method == "POST":
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            post = Post(title, img_url, caption, current_user.id)

            db.session.add(post)
            db.session.commit()   

            return redirect(url_for('home'))         

    return render_template('createpost.html', form = form)

@ig.route('/posts/<int:post_id>')
def individualPost(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return redirect(url_for('ig.posts'))
    return render_template('individual_post.html', post = post)

@ig.route('/posts/update/<int:post_id>', methods=["GET","POST"])
@login_required
def updatePost(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return redirect(url_for('ig.posts'))
    if post.user_id != current_user.id:
        return redirect(url_for('ig.posts'))
    form = UpdatePostForm()
    if request.method == "POST":
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            # update the original post
            post.title = title
            post.image = img_url
            post.caption = caption

            db.session.commit()   

            return redirect(url_for('home'))         
    return render_template('updatepost.html', form=form, post = post)


@ig.route('/posts/delete/<int:post_id>', methods=["POST"])
@login_required
def deletePost(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return redirect(url_for('ig.posts'))
    if post.user_id != current_user.id:
        return redirect(url_for('ig.posts'))

    db.session.delete(post)
    db.session.commit()
               
    return redirect(url_for('ig.posts'))



#
#
# API Stuff
#
#

@ig.route('/api/tools')
def apiPosts():
    tools = Inventory.query.all()[::-1]
    return {
        'status': 'ok',
        'total_results': len(tools),
        'tools': [t.to_dict() for t in tools],
        }