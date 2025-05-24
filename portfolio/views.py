from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """View principal do portfólio"""
    context = {
        'skills': [
            {'name': 'Python', 'icon': 'fab fa-python', 'level': 90},
            {'name': 'R', 'icon': 'fab fa-r-project', 'level': 85},
            {'name': 'SQL', 'icon': 'fas fa-database', 'level': 88},
            {'name': 'Pandas', 'icon': 'fas fa-table', 'level': 92},
            {'name': 'NumPy', 'icon': 'fas fa-calculator', 'level': 87},
            {'name': 'Scikit-learn', 'icon': 'fas fa-brain', 'level': 85},
            {'name': 'TensorFlow', 'icon': 'fas fa-robot', 'level': 80},
            {'name': 'Matplotlib', 'icon': 'fas fa-chart-line', 'level': 88},
            {'name': 'Seaborn', 'icon': 'fas fa-chart-bar', 'level': 85},
            {'name': 'Power BI', 'icon': 'fas fa-chart-pie', 'level': 82},
            {'name': 'Tableau', 'icon': 'fas fa-desktop', 'level': 78},
            {'name': 'Git', 'icon': 'fab fa-git-alt', 'level': 85},
        ],
        'projects': [
            {
                'id': 1,
                'title': 'Análise de Vendas E-commerce',
                'short_description': 'Dashboard interativo para análise de vendas e comportamento do cliente',
                'image': '/static/images/project1.jpg',
                'full_description': 'Projeto completo de análise de dados de um e-commerce, incluindo análise exploratória de dados, segmentação de clientes usando K-means, previsão de vendas com modelos de machine learning e criação de dashboard interativo no Power BI. Utilizei Python, Pandas, Scikit-learn e Power BI para entregar insights valiosos sobre o comportamento dos clientes e tendências de vendas.',
                'technologies': ['Python', 'Pandas', 'Scikit-learn', 'Power BI', 'SQL'],
                'github_link': 'https://github.com/seu-usuario/ecommerce-analysis'
            },
            {
                'id': 2,
                'title': 'Previsão de Preços Imobiliários',
                'short_description': 'Modelo de machine learning para predição de preços de imóveis',
                'image': '/static/images/project2.jpg',
                'full_description': 'Desenvolvimento de um modelo preditivo robusto para preços de imóveis utilizando técnicas avançadas de machine learning. O projeto incluiu web scraping para coleta de dados, feature engineering, teste de múltiplos algoritmos (Random Forest, XGBoost, Linear Regression) e validação cruzada. O modelo final alcançou 92% de acurácia na previsão de preços.',
                'technologies': ['Python', 'XGBoost', 'BeautifulSoup', 'Matplotlib', 'Seaborn'],
                'github_link': 'https://github.com/seu-usuario/house-price-prediction'
            },
            {
                'id': 3,
                'title': 'Análise de Sentimentos - Redes Sociais',
                'short_description': 'Sistema de análise de sentimentos em tempo real para tweets',
                'image': '/static/images/project3.jpg',
                'full_description': 'Sistema completo de análise de sentimentos em tempo real utilizando NLP para processar tweets sobre marcas específicas. Implementei pipeline de processamento de texto, modelo de deep learning com LSTM, API para coleta de dados do Twitter e dashboard em tempo real. O projeto ajudou empresas a monitorar sua reputação online.',
                'technologies': ['Python', 'TensorFlow', 'LSTM', 'Twitter API', 'Flask'],
                'github_link': 'https://github.com/seu-usuario/sentiment-analysis'
            },
            {
                'id': 4,
                'title': 'Sistema de Recomendação',
                'short_description': 'Engine de recomendação para plataforma de streaming',
                'image': '/static/images/project4.jpg',
                'full_description': 'Desenvolvimento de um sistema de recomendação híbrido combinando filtragem colaborativa e baseada em conteúdo para uma plataforma de streaming. Utilizei algoritmos de matrix factorization, deep learning e processamento de linguagem natural para analisar preferências dos usuários. O sistema aumentou o engajamento em 35%.',
                'technologies': ['Python', 'TensorFlow', 'Surprise', 'NLP', 'MongoDB'],
                'github_link': 'https://github.com/seu-usuario/recommendation-system'
            }
        ]
    }
    return render(request, 'portfolio/home.html', context)

@csrf_exempt
def send_contact_email(request):
    """View para enviar email de contato"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            
            # Compor email
            email_subject = f'Contato do Portfólio: {subject}'
            email_message = f"""
            Nome: {name}
            Email: {email}
            Assunto: {subject}
            
            Mensagem:
            {message}
            """
            
            # Enviar email
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ['seu-email@gmail.com'],  # Substitua pelo seu email
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'message': 'Email enviado com sucesso!'})
            
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Erro ao enviar email.'})
    
    return JsonResponse({'success': False, 'message': 'Método não permitido.'})

def get_project_detail(request, project_id):
    """View para retornar detalhes do projeto via AJAX"""
    projects = {
        1: {
            'title': 'Análise de Vendas E-commerce',
            'full_description': 'Projeto completo de análise de dados de um e-commerce, incluindo análise exploratória de dados, segmentação de clientes usando K-means, previsão de vendas com modelos de machine learning e criação de dashboard interativo no Power BI. Utilizei Python, Pandas, Scikit-learn e Power BI para entregar insights valiosos sobre o comportamento dos clientes e tendências de vendas.',
            'technologies': ['Python', 'Pandas', 'Scikit-learn', 'Power BI', 'SQL'],
            'github_link': 'https://github.com/seu-usuario/ecommerce-analysis'
        },
        2: {
            'title': 'Previsão de Preços Imobiliários',
            'full_description': 'Desenvolvimento de um modelo preditivo robusto para preços de imóveis utilizando técnicas avançadas de machine learning. O projeto incluiu web scraping para coleta de dados, feature engineering, teste de múltiplos algoritmos (Random Forest, XGBoost, Linear Regression) e validação cruzada. O modelo final alcançou 92% de acurácia na previsão de preços.',
            'technologies': ['Python', 'XGBoost', 'BeautifulSoup', 'Matplotlib', 'Seaborn'],
            'github_link': 'https://github.com/seu-usuario/house-price-prediction'
        },
        3: {
            'title': 'Análise de Sentimentos - Redes Sociais',
            'full_description': 'Sistema completo de análise de sentimentos em tempo real utilizando NLP para processar tweets sobre marcas específicas. Implementei pipeline de processamento de texto, modelo de deep learning com LSTM, API para coleta de dados do Twitter e dashboard em tempo real. O projeto ajudou empresas a monitorar sua reputação online.',
            'technologies': ['Python', 'TensorFlow', 'LSTM', 'Twitter API', 'Flask'],
            'github_link': 'https://github.com/seu-usuario/sentiment-analysis'
        },
        4: {
            'title': 'Sistema de Recomendação',
            'full_description': 'Desenvolvimento de um sistema de recomendação híbrido combinando filtragem colaborativa e baseada em conteúdo para uma plataforma de streaming. Utilizei algoritmos de matrix factorization, deep learning e processamento de linguagem natural para analisar preferências dos usuários. O sistema aumentou o engajamento em 35%.',
            'technologies': ['Python', 'TensorFlow', 'Surprise', 'NLP', 'MongoDB'],
            'github_link': 'https://github.com/seu-usuario/recommendation-system'
        }
    }
    
    project = projects.get(int(project_id))
    if project:
        return JsonResponse(project)
    else:
        return JsonResponse({'error': 'Projeto não encontrado'}, status=404)