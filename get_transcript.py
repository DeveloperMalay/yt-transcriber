from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import sys

def extract_video_id(url_or_id: str) -> str:
    if len(url_or_id) == 11 and ('/' not in url_or_id):
        return url_or_id
    parsed = urlparse(url_or_id)
    if parsed.netloc.endswith("youtu.be"):
        return parsed.path.lstrip("/")
    qs = parse_qs(parsed.query)
    if "v" in qs:
        return qs["v"][0]
    return url_or_id

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url:
        print("Usage: python get_transcript.py <youtube_url>")
        sys.exit(1)
    video_id = extract_video_id(url)

    print(f"Fetching transcript for video ID: {video_id}")
    
    try:
        api = YouTubeTranscriptApi()
        
        # List available transcripts
        transcript_list = api.list(video_id)
        print(f"Available transcripts: {[t.language_code for t in transcript_list]}")
        
        # Try to get English transcript, fallback to any available
        try:
            transcript_data = api.fetch(video_id, languages=['en'])
            print("Using English transcript")
        except:
            transcript_data = api.fetch(video_id)
            print("Using auto-detected language transcript")
        
        for seg in transcript_data:
            start = seg.start
            text = seg.text
            print(f"[{start:7.2f}] {text}")
            
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        print(f"Error type: {type(e).__name__}")