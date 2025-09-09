using MongoDB.Driver;

using MongoDB.Bson;
using System;
using System.Threading.Tasks;
class Program
{
    static async Task Main(string[] args)
    {
        // Anslutningssträng från MongoDB Atlas
        string anslutningsstrang =
        "mongodb+srv://minAppUser:DITT_LÖSENORD@cluster0.xxxxx.mongodb.net/?retryWri
    tes = true & w = majority";
    var client = new MongoClient(anslutningsstrang);
        // Välj databas och samling
        var db = client.GetDatabase("MinSkola");
        var samling = db.GetCollection<BsonDocument>("elever");
        // ---- SKAPA DATA ----
        var nyElev = new BsonDocument
{
{ "namn", "Cecilia Ceder" },
{ "program", "Samhällsvetenskap" },
{ "årskurs", 1 },
{ "kurser", new BsonArray { "Samhällskunskap", "Historia" } }
};
        await samling.InsertOneAsync(nyElev);
        Console.WriteLine($"Lade till eleven: {nyElev["namn"]}");
        // ---- HÄMTA DATA ----
        Console.WriteLine("\nSöker efter Cecilia...");
        var filter = Builders<BsonDocument>.Filter.Eq("namn", "Cecilia Ceder");
        var hittadElev = await samling.Find(filter).FirstOrDefaultAsync();

        if (hittadElev != null)
        {
            Console.WriteLine($"Hittade eleven: {hittadElev["namn"]}, som går i årskurs
        { hittadElev["årskurs"]}
            ");
        }
        else
        {
            Console.WriteLine("Kunde inte hitta eleven.");
        }
    }
}