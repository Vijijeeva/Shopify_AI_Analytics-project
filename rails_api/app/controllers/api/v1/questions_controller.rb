module Api
  module V1
    class QuestionsController < ApplicationController
      def create
        store_id = params[:store_id]
        question = params[:question]

        if store_id.blank? || question.blank?
          return render json: { error: "Invalid input" }, status: 400
        end

        response = PythonAiService.ask_question(store_id, question)

        render json: response
      end
    end
  end
end
