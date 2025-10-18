# How to Find Your Weaviate Cluster URL

Your Weaviate cluster has a UUID: `acb13d12-5c36-4253-9d71-746717093f80`

## Step-by-Step Instructions

### Option 1: Check the Weaviate Cloud Console

1. **Go to your cluster details page**:
   https://console.weaviate.cloud/cluster-details/acb13d12-5c36-4253-9d71-746717093f80

2. **Look for one of these sections on that page**:
   - "Cluster URL"
   - "REST Endpoint"
   - "Connection Details"
   - "API Endpoint"

3. **Copy the URL shown there**. It will look like ONE of these formats:

   **Format A (most common for newer clusters):**
   ```
   https://acb13d12-5c36-4253-9d71-746717093f80.weaviate.network
   ```

   **Format B (WCS clusters):**
   ```
   https://your-cluster-name-acb13d12.wcs.api.weaviate.cloud
   ```

   **Format C (older format):**
   ```
   https://something.weaviate.cloud
   ```

### Option 2: Common URL Pattern

Based on your cluster UUID, the most likely URL is:

```
https://acb13d12-5c36-4253-9d71-746717093f80.weaviate.network
```

Try this first! If it doesn't work, check the console.

### Option 3: Use the Weaviate Cloud API

If you can't find it in the console, you might need to:

1. Log into Weaviate Cloud Console
2. Click on your cluster name (not the UUID)
3. Look for a "Details" or "Connect" tab
4. There should be example code showing the connection - copy the URL from there

## What NOT to Use

❌ **DO NOT USE**: `https://console.weaviate.cloud/cluster-details/...`
   - This is the CONSOLE page, not the API endpoint

❌ **DO NOT USE**: URLs with `/cluster-details/` in them
   - These are web UI pages, not API endpoints

## Testing Your URL

Once you have the URL, you can test it:

```bash
# Test with curl (should return cluster metadata)
curl https://YOUR-CLUSTER-URL.weaviate.network/v1/meta

# Or test with Python
./venv/bin/python3 test_weaviate.py
```

## Still Can't Find It?

If you still can't find the cluster URL:

1. **Check if the cluster is running**:
   - In the console, check the cluster status (should be "Running" or "Ready")

2. **Look for a "Connect" or "API Keys" section**:
   - Often the connection details are shown when you manage API keys

3. **Check the cluster creation confirmation email**:
   - Weaviate usually emails you the connection details when you create a cluster

4. **Contact Weaviate Support**:
   - If this is a work/company cluster, ask your team
   - Or check Weaviate's Slack/Discord community

## Screenshot of Where to Look

In the Weaviate Cloud Console, you should see something like:

```
┌─────────────────────────────────────────────┐
│ Cluster Details                              │
├─────────────────────────────────────────────┤
│ Name: My Cluster                            │
│ Status: ● Running                           │
│ Cluster URL: https://xxx.weaviate.network   │  ← THIS IS WHAT YOU NEED!
│ API Key: [Manage Keys]                      │
└─────────────────────────────────────────────┘
```

---

**TIP**: The cluster URL is needed to actually CONNECT to your data. The console URL is just for managing the cluster through the web interface.
