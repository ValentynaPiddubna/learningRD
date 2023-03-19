const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'Indigo';
myDiv.style.textAlign = 'center';

let i = (Math.random() * (1000 - 1) + 1).toFixed();

const friends = document.createElement('div');
friends.className = 'friends';
friends.innerText = `# Friends: ${i}`


const buttonsNames = ['Add Friend', 'Message', 'Offer a job']

buttonsNames.map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText = `${buttonName}`;
    button.style.margin = '5px';
    button.style.borderRadius = '5px';
    myDiv.appendChild(button);
})

document.getElementsByTagName('body')[0].appendChild(myDiv);
myDiv.after(friends);

// events

const btn = document.getElementsByTagName('button')[0];

btn.onclick = (event) => {
    event.target.innerText = `Confirmation is pending`;
    friends.innerText = `# Friends: ${++i}`;
};


btn.addEventListener('click', (myButtonEvent) => {
    myButtonEvent.target.style.background = '#ecf2f9';
    myButtonEvent.target.style.color = '#00204a';
    myButtonEvent.target.disabled = true;
});


const btn2 = document.getElementsByTagName('button')[1];

btn2.onclick = (event) => {

    let currentBackground = btn2.style.background;

    event.target.style.background = currentBackground !== 'blue' ? 'blue' : '#198754';

};

