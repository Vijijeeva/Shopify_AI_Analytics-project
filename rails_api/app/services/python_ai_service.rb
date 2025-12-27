require 'net/http'
require 'json'

class PythonAiService
  def self.ask_question(store_id, question)
    uri = URI("http://localhost:8000/ask")

    http = Net::HTTP.new(uri.host, uri.port)
    request = Net::HTTP::Post.new(uri.path, { 'Content-Type': 'application/json' })
    request.body = {
      store_id: store_id,
      question: question
    }.to_json

    response = http.request(request)
    JSON.parse(response.body)
  rescue
    { error: "Python AI service not available" }
  end
end
