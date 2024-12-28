let PostForm = document.getElementById("PostForm");

PostForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    let PostData = {
        title: e.target[0].value,
        poster: e.target[1].value,
        content: e.target[2].value,
    }
    console.log(PostData);
    let res = await axios.post("http://127.0.0.1:8000/post/createPost/", PostData);
    console.log(res.data);

})