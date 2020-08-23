const el = (tagName, attributes, children) => {
    const element = document.createElement(tagName);
    if (attributes) {
        for (const attrName in attributes) {
            element.setAttribute(attrName, attributes[attrName]);
        }
    }
    if (children) {
        for (let i = 0; i < children.length; i++) {
            const child = children[i];

            if (typeof child === 'string') {
                element.appendChild(document.createTextNode(child));
            } else {
                element.appendChild(child);
            }
        }
    }
    return element;
};

const div = (a, c) => el('div', a, c);
const img = (a,c) => el('img', a, c);

const rankVals = '1 2 3 4 5'.split(' ');
const multiplicity = [3, 2, 2, 2, 1];

let ranksTemp = [];
for (let ind = 0; ind < rankVals.length; ++ind) {
    for (let i = 0; i < multiplicity[ind]; ++i) {
        ranksTemp.push(rankVals[ind])
    }
}
const ranks = ranksTemp

// console.log([i for (i in )]);
console.log(ranks);
const colors = ['red','blue','green','yellow','white']
const getRank = (i) => ranks[i % 10]
const getColor = (i) => colors[i/10 | 0];

const createCard = (i) => {
    const imgName = 'images/firework1.png'
    const rank = getRank(i);
    const color = getColor(i);
    console.log(i, color);
    return div({class: 'card-container', id: i, onclick:"playCard(this.id)"}, [
        div({class: 'card'}, [
            div({class: 'face ' + color}, [
                div({class: 'face-top-left'}, [
                    div({class: 'face-corner-rank'}, [rank])
                ]),
                img({class: 'face-icon', src: imgName},[]),
                div({ class: 'face-bottom-right' }, [
                    div({ class: 'face-corner-rank' }, [rank])
                ])
            ]),
            div({class: 'back'}, [
                img( {src: 'images/pagoda.png'},[])
            ])
        ])
    ]);
};

let cardsData = new Array(50);

for (let i = 0; i < cardsData.length; ++i) {
    cardsData[i] = i
}


let deckArray = []
cardsData.forEach((i) => {
    deckArray.push(createCard(i))
});
const deck = div({ class: 'deck' }, deckArray);

// document.body.appendChild(deck);
const createHand = () => {
    let arr = []
    for (let i = 0; i < 5; ++i) {
        let multi = 7;
        arr.push(deckArray[deckArray.length-1]);
        deckArray.pop()
    }
    return arr;
};
/*
document.body.appendChild(
    div({class: 'active-hand'},[
        createCard(10)
    ])
);

document.body.appendChild(
    div({class: 'active-hand'},[
        createCard(2),
        createCard(2),
        createCard(2),
        createCard(2),
        createCard(2)
    ])
);


document.body.appendChild(
    div({class: 'hand active-hand'}, [
        div({class: 'group'},
            createHand()
        )
    ])
);*/
const createPlayer = () => {
    return div({class: 'group'}, [
        div({class: 'hand'}, createHand())
    ])
};
function playCard(id) {
    document.getElementById(id).remove();
}

let board = document.body.appendChild(
    div({class: 'group'}, [
        div({class: 'pile'}, createHand()),
        div({class: 'pile'}, createHand()),
        div({class: 'pile'}, createHand()),
        div({class: 'pile'}, createHand()),
        div({class: 'pile'}, createHand())
    ])
);

document.body.appendChild(
    div({class: 'table'},[
        div({class: 'section other-players-hands'},[
            div({class: 'group'}, [
                div({class: 'hand'}, createHand()),
                div({class: 'hand'}, createHand()),
                div({class: 'hand'}, createHand()),
                div({class: 'hand'}, createHand())
            ])
        ]),
        div({class: 'section board'},[
            board
        ]),
        div({class: 'section your-hand'},[
            createPlayer()
        ])
    ])
);

/*

*/

/*
hands = div({class: 'hand active-hand'},[
    div({class: 'group pile'}, createHand()),
    div({class: 'group pile'}, createHand()),
    div({class: 'group pile'}, createHand()),
    div({class: 'group pile'}, createHand()),
    div({class: 'group pile'}, createHand())
])
document.body.appendChild(hands);

html = div({class: 'table'}, [
    div({class: 'section other-players-hands'},[]),
    div({class: 'section board'},[
        hands
    ]),
    div({class: 'section your-hand'},[])
]);
document.body.appendChild(html);
*/



