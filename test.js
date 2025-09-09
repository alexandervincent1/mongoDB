const { MongoClient } = require('mongodb');
// Anslutningssträng från MongoDB Atlas
const anslutningsstrang =
"mongodb+srv://alexandervincent_db_user:UQ3vRAUst_pA6_b@cluster0.dozqe8u.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(anslutningsstrang);
async function run() {
try {
// Anslut till servern
await client.connect();
console.log("Ansluten till databasen!");
// Välj databas och samling
const db = client.db('MinSkola');
const samling = db.collection('elever');
// ---- SKAPA DATA ----
const nyElev = {
namn: "Bengt Bengtsson",
program: "Ekonomi",

årskurs: 3,
kurser: ["Företagsekonomi", "Marknadsföring"]
};
await samling.insertOne(nyElev);
console.log(`Lade till eleven: ${nyElev.namn}`);
// ---- HÄMTA DATA ----
console.log("\nSöker efter Bengt...");
const hittadElev = await samling.findOne({ namn: "Bengt Bengtsson" });
if (hittadElev) {
console.log(`Hittade eleven: ${hittadElev.namn}, som går i årskurs
${hittadElev.årskurs}`);
} else {
console.log("Kunde inte hitta eleven.");
}

} finally {
// Stäng anslutningen när vi är klara
await client.close();
}
}
// Kör funktionen och fånga eventuella fel
run().catch(console.dir);