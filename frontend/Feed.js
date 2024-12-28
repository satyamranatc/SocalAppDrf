let container = document.getElementsByClassName("container")[0];

let AllPostsData = []
async function GetData()
{

    let AllPost = await axios.get("http://127.0.0.1:8000/post/allPosts/");
    console.log(AllPost.data);
    AllPostsData = AllPost.data;
    DisplayData(AllPostsData);
}
GetData();




// Function to Display The Post Omn Conatiner Div:
function DisplayData(data)
{
    data.forEach(post => {
        container.innerHTML += `
             <div class="post">
            <div class="post-header">
                <img src="https://placehold.co/600x400" alt="User">
                <div>
                    <h3>${post.title}</h3>
                    <p style="color: #65676b; font-size: 0.8rem;">${post.created_at}</p>
                </div>
            </div>
            <div class="post-content">
                <img src="${post.poster}" alt="Post">
            </div>
            <div class="post-text">
                <p>${post.content}</p>
            </div>
            <div class="post-actions">
                <button class="post-action-btn">
                    <i data-lucide="heart"></i>
                    Like
                </button>
                <button class="post-action-btn">
                    <i data-lucide="message-circle"></i>
                    Comment
                </button>
                <button class="post-action-btn">
                    <i data-lucide="share-2"></i>
                    Share
                </button>
            </div>
        </div>
        `
    });
   
}