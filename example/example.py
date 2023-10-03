import sys
sys.path.append("..")

from sdk.main import Connect
from dotenv import load_dotenv
import os

# load ENV file
load_dotenv()

# To connect you most provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables

# Create a client that is authed against the API
client = Connect(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

# list sources
sources = client.source.list_sources()
print("Found ", len(sources.data), " sources")

# get the first source
firstSource = client.source.get_source(sources.data[0].id)
print("First source is: ",firstSource.label)

# search for an entity
search_term = "Slickdeals"
entitySearchResults = client.search.search_entity(q=search_term)
print("Found ", len(entitySearchResults.data), " entity results for ", search_term)

firstEntityResult = entitySearchResults.data[0].id

# get entity summary
entitySummary = client.entity.entity_summary(firstEntityResult)
print("Has address: ", entitySummary.addresses[0])

# get the full entity
entityDetails = client.entity.get_entity(firstEntityResult)
print("Is referenced by ", len(entityDetails.referenced_by.data), " sources")

# resolve
resolution = client.resolution.resolution(name=search_term)
print(resolution)

"""
// Resolve
resolution, err := client.Resolution.Resolution(context.Background(), &sayari.Resolution{Name: []*string{&searchTerm}})
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(resolution)
log.Printf("Resolved to %v entities.", len(resolution.Data))

// Search for record
recordSearch, err := client.Search.SearchRecord(context.Background(), &sayari.SearchRecord{Q: searchTerm})
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(recordSearch)
log.Printf("Found %v records.", len(recordSearch.Data))

// Get record
record, err := client.Record.GetRecord(context.Background(), url.QueryEscape(recordSearch.Data[0].Id), &sayari.GetRecord{})
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(record)
log.Printf("Found record: %v.", record.Label)

// Do traversal
traversal, err := client.Traversal.Traversal(context.Background(), firstEntityResult, &sayari.Traversal{})
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(traversal)
log.Printf("Did traversal of entity %v. Found %v related things.", firstEntityResult, len(traversal.Data))

// Do UBO traversal
ubo, err := client.Traversal.Ubo(context.Background(), firstEntityResult)
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(ubo)
log.Printf("Found %v beneficial owners.", len(ubo.Data))

// Ownership
downstream, err := client.Traversal.Ownership(context.Background(), ubo.Data[0].Target.Id)
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(downstream)
log.Printf("Found %v downstream things owned by the first UBO of %v.", len(downstream.Data), searchTerm)

// Fetch an entity likely to be associated with watch lists
putinResult, err := client.Search.SearchEntity(context.Background(), &sayari.SearchEntity{Q: "putin"})
if err != nil {
    log.Fatalf("Error: %v", err)
}
// Check watchlist
watchlist, err := client.Traversal.Watchlist(context.Background(), putinResult.Data[0].Id)
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(watchlist)
log.Printf("Found %v watchlist resulsts for entity %v.", len(watchlist.Data), putinResult.Data[0].Id)

// Shortest Path
shortestPath, err := client.Traversal.ShortestPath(context.Background(), &sayari.ShortestPath{Entities: []string{firstEntityResult, ubo.Data[0].Target.Id}})
if err != nil {
    log.Fatalf("Error: %v", err)
}
// uncomment to view data
//spew.Dump(shortestPath)
log.Printf("Found path with %v hops", len(shortestPath.Data[0].Path))
"""
