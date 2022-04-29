<?php

namespace App\Controller;

use App\Entity\Campaigns;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Tags;

class MainController extends AbstractController
{
    /**
     * @Route("/", name="index_page")
     */
    public function index(): Response
    {
        $campaigns = '';

        $user = $this->getUser();
        if ($user) {
            $campaigns = $this->getDoctrine()->getRepository(Campaigns::class)->findBy([],['id' => 'DESC'],10);
        }

        $tags_campaign = $this->getDoctrine()->getRepository(Tags::class)->findBy([],['id' => 'DESC'],20);

        return $this->render('main/index.html.twig', [
            'campaigns' => $campaigns,
            'tags' => $tags_campaign,
        ]);
    }
}
