// Description: Randomizes the cohort then pairs two of them together. 
// Whoever is left is solo

// Names Excluded:"Asanda", "Phomello", "Cadee", "Lesedi"
let cohort = ["Aidan", "Courtney", "Ethan", "Lindo", "Pierre", "Ronny", "Sibu", "Tom", "Ulrich", "Mieke", "Marvelous"];

// Shuffle the cohort array
for (let i = cohort.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cohort[i], cohort[j]] = [cohort[j], cohort[i]];
}

// Pair students together
let pairs = [];
while (cohort.length > 1) {
    let pair = [cohort.pop(), cohort.pop()];
    pairs.push(pair);
}

// If there's an odd number of students, the last one is left alone
let leftAlone = cohort.length === 1 ? cohort[0] : null;

// Print the pairs and the student left alone
pairs.forEach(pair => {
    console.log(`Pair: ${pair[0]} with ${pair[1]}`);
});

if (leftAlone) {
    console.log(`Solo: ${leftAlone}`);
}